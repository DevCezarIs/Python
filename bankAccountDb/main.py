import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "BankSys.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela_clientes(conexao, cursor):
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS clientes (
        clientId INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        tel VARCHAR(150),
        data_cadastro DATE
    );
    """
    )

def criar_tabela_conta(conexao, cursor):
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS conta (
        contaId INTEGER PRIMARY KEY AUTOINCREMENT,
        clientId INTEGER,
        saldo REAL DEFAULT 0.00,
        data_abertura DATE,
        tipo VARCHAR(20),
        FOREIGN KEY (clientId) REFERENCES clientes(clientId)
    );
    """
    )

def criar_tabela_transacoes(conexao, cursor):
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS transacoes (
        transacaoId INTEGER PRIMARY KEY AUTOINCREMENT,
        id_conta_origem INTEGER,
        id_conta_destino INTEGER,
        tipo VARCHAR(20),
        valor REAL,
        data DATE,
        FOREIGN KEY (id_conta_origem) REFERENCES conta(contaId),
        FOREIGN KEY (id_conta_destino) REFERENCES conta(contaId)
    );
    """
    )
criar_tabela_clientes(conexao, cursor)
criar_tabela_conta(conexao, cursor)
criar_tabela_transacoes(conexao, cursor)