import sqlite3 as conector

conexao = conector.connect("fabrica543.db")
cursor = conexao.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS devs(
               id_dev INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome VARCHAR (60),
               area_atuacao VARCHAR (200),
               telefone VARCHAR (14)
               )""")

# cursor.execute(""" INSERT INTO devs(nome, area_atuacao, telefone) VALUES ('Carlos', 'Computaria', '6996969')""")

# nomeDev = input("Digite o nome do meliante: ")
# area = input("Digite a área de atuação do cabra: ")
# telefone = input("Digite o telefone do peste: ")

# cursor.execute(""" INSERT INTO devs(nome, area_atuacao, telefone) VALUES (?, ?, ?)""", (nomeDev, area, telefone))

cursor.execute("""SELECT * FROM devs""")

dados = cursor.fetchall()

for i in dados:
    print(i)


conexao.commit()