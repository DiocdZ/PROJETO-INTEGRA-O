import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS
from requests import JSONDecodeError

def pega_conexao():
    nome_banco = "BANCO DE DADOS/TCC - BANCO DE DADOS.db" 
    con = sqlite3.connect(nome_banco) # conecta ao banco
    return con

# # Aplicação web com Flask
app = Flask(__name__)
CORS(app)

@app.route('/')
def raiz():
    return "resposta do meu backend em python!"

@app.route("/todos")
def todos():
    con = pega_conexao()
    cur = con.cursor()
    
    try:
        cur.execute("SELECT * FROM Videos")
    except:
        con.close()
        return jsonify("Erro ao consultar o banco")
    
    dados = cur.fetchall()
    con.close()
    return jsonify(dados)

@app.route("/mostra/<int:id>") #http://localhost:5000/lista/1
def mostra_um(id):
    con = pega_conexao()
    cur = con.cursor()

    try:
        cur.execute(f"SELECT * FROM Videos WHERE id={id}")
    except:
        con.close()
        return jsonify("Erro ao consultar o banco")

    dados = cur.fetchone()
    con.close()
    return jsonify(dados)

@app.route("/videos/<int:pagina>")
def videos(pagina):
    con = pega_conexao()
    cur= con.cursor()

    try:
        quantidade = 3
        offset = (pagina -1)* quantidade
        cur.execute(f"SELECT * FROM Videos ORDER by id ASC LIMIT {quantidade} OFFSET {offset}")
    except:
        con.close()
        return jsonify("erro ao consultar banco")

    dados= cur.fetchall()

    return jsonify(dados)

if __name__ == "__main__":
	app.run()

    