import sqlite3 as conector

conexao = conector.connect("fabrica543.db")
cursor = conexao.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS devs(
               id_dev INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome VARCHAR (60),
               area_atuacao VARCHAR (200),
               telefone VARCHAR (14)
               )""")

conexao.commit()

def cadastrar():
    
    nomeDev = input("Digite o nome do meliante: ")
    area = input("Digite a área de atuação do cabra: ")
    telefone = input("Digite o telefone do peste: ")

    cursor.execute(""" INSERT INTO devs(nome, area_atuacao, telefone) VALUES (?, ?, ?)""", (nomeDev, area, telefone))

    conexao.commit()

    print("Cadastro realizado com sucesso!")

def listar():
    
    cursor.execute("""SELECT * FROM devs""")

    dados = cursor.fetchall()

    if not dados:
        print("nenhum dev cadastrado")
        return
    
    print('\n LISTA DE DEVS')
    for i in dados:
        print(f"ID: {i[0]} | Nome: {i[1]} | Área de atuação: {i[2]} | Telefone: {i[3]}")

def atualizar():
    listar()
    id_dev = int(input('\nDigite o id do dev que deseja atualizar: '))

    nomeDev = input("Novo nome: ")
    atuacao = input('Nova área de atuação: ')
    telefone = input('Novo Telefone: ')

    cursor.execute(""" UPDATE devs SET nome = ?, area_atuacao = ?, telefone = ? where id_dev = ?""", (nomeDev, atuacao, telefone, id_dev))

    conexao.commit()

    print("Dados atualizados com sucesso!")

def deletar():
    listar()
    id_dev = int(input("\nDigite o ID do usuário que desejar deletar: "))

    cursor.execute("""DELETE FROM devs WHERE id_dev = ?""", (id_dev,))

    conexao.commit()

    print("\nUsuário deletado com sucesso!")

def menu():
    while True:
        print("\n====== MENU ======")
        print("1 - Cadastrar DEV")
        print("2 - Lista DEV")
        print("3 - Atualizar DEV")
        print("4 - Deletar DEV")
        print("5 - Sair")

        opcao = int(input("Resposta:"))

        match opcao:
            case 1:
                cadastrar()

            case 2:
                listar()

            case 3: 
                atualizar()

            case 4: 
                deletar()

            case 5:
                break

            case _:
                continue

menu()

conexao.close()