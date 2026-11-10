import sqlite3
conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

cursor.execute(" CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, quantidade INTEGER, preco currency)")
conn.commit()

vnome = "Pastel"
vquantidade = 3
vpreco = 14

cursor.execute("INSERT INTO produtos (nome,quantidade,preco) VALUES (?,?,?)", (vnome,vquantidade,vpreco))

conn.commit
cursor.execute('SELECT * FROM produtos')

registros = cursor.fetchall() 
for linha in registros: 
    print(f"ID: {linha[0]} | Nome: {linha[1]} | Quantidade: {linha[2]} Preco: {linha[3]}") 