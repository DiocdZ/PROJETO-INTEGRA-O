import sqlite3

nome_banco = "tcc_banco_de_dado.db"
con = sqlite3.connect(tcc_banco_de_dado.db)
cur = con.cursor()

videos = [
    (Titulo, 'COMECOU! O inicio da batalha de Yoh! #ShamanKing (2021) [Review episódios 1 e 2]', 'https://youtu.be/Yx5mGe6Oi50','https://img.youtube.com/vi/Yx5mGe6Oi50/hqdefault.jpg'),
    (Titulo, 'O PAU COMEU! Chegou Lee Payron! #ShamanKing 2021 [Review episódio 3]','https://youtu.be/nvH_a5pJbBg','https://img.youtube.com/vi/nvH_a5pJbBg/hqdefault.jpg'),
    (Titulo, 'O MELHOR ANIME MUSICAL? Muito punk, lagrimas e corações partidos #NANA! [INDICAÇÃO]', "https://youtu.be/PazNAq5vDUc","https://img.youtube.com/vi/PazNAq5vDUc/hqdefault.jpg",)
]

cur.executemany("INSERT INTO Videos VALUES (?, ?, ?)", videos)

con.commit()
con.close()