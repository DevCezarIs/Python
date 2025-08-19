import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Insira o id do cliente: ")
cursor.execute(f"SELECT * FROM clientes WHERE id=?", (id_cliente))
clientes = cursor.fetchall()

for row in clientes:
    print((f"O ID do cliente é {row["id"]}"))