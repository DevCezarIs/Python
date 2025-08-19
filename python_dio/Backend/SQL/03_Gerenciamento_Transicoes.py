import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("INSERT INTO clientes(nome,email) VALUES(?,?)", ("TESTE_1", "TESTE_1@gmail.com;"))
    cursor.execute("INSERT INTO clientes(id,nome,email) VALUES(?,?,?);", (9, "TESTE_1", "TESTE_1@gmail.com"))
    conexao.commit()
    

except Exception as exp:
    print(f"Ops ocorreu um erro: {exp}")
    conexao.rollback()