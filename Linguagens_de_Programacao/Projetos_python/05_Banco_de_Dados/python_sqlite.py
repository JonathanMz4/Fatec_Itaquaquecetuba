# VAMOS UTILIZAR PYTHON E BANCO DE DADOS SQLITE 3

# C.R.U.D:
# CREATE (INSET), READ (SELECT), UPDATE (UPDATE), DELETE (DELETE)

import sqlite3
conn = sqlite3.connect('empresa.db') #conn é conexão
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXITS clientes ( id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT UNIQUE)")conn.commit()

vnome = "Ana Silva" vemail = "ana@gmail.com" cursos.execute("INSERT INTO cliente (nome,email) VALUES (?,?)", (vnome, vemail))
#Uso seguro com parametros
conn.commit() 
