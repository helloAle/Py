import sqlite3

conexao = sqlite3.connect("banco.db") #vai passar como string o caminho pro banco de dados
cursor = conexao.cursor() # cursor obsejo mensageiro entre o banco de dados e o python

# UM BANCO DE DADOS FUNCIONA COMO UMA TABELA :p

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               titular TEXT NOT NULL,
               saldo FLOAT NOT NULL,
               cpf TEXT NOT NULL UNIQUE
               )""")

# cursor.execute("""INSERT INTO contas_bancarias
#                (titular, saldo, cpf) VALUES
#                ('Ale', -7000, '123456789')""")

cursor.execute("""SELECT titular, saldo FROM contas_bancarias""")
contas = cursor.fetchall()
for conta in contas:
    titular, saldo = conta
    print(f"""titular: {titular}
saldo: {saldo}\n""")

conexao.commit()