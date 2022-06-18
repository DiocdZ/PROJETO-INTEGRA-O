# #import sqlite3
# import os.path
# import os

# nome_banco = "tcc_banco_de_dado.db"

# if os.path.exists(tcc_banco_de_dado):
#     os.unlink(tcc_banco_de_dado)

# conexao = sqlite3.connect(tcc_banco_de_dado)
# cursor = conexao.cursor()

# consulta = """CREATE TABLE "Videos" (
#     id INTEGER UNIQUE, "TITULO"TEXT, "LINK-URL"TEXT, "THUMB"TEXT
#     PRIMARY KEY ("id"  AUTOINCREMENT))
#     """
# cursor.execute(consulta)

# #conexao.close()#