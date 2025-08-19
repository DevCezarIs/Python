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

class Cliente:
    def __init__(self,conta_id, nome, tel, data_cadastro):
        self.nome = nome
        self.conta_id = conta_id
        self.tel = tel
        self.data_cadastro = data_cadastro

class Conta:
    def __init__(self, client_id, saldo, tipo, data_abertura):
        
        self.client_id = client_id
        self.saldo = saldo
        self.tipo = tipo
        self.data_abertura = data_abertura
    
    def deposito(self,cursor,conta_id, conexao, valor ):
        if valor > 0:
            cursor.execute("UPDATE conta SET saldo = saldo + ? WHERE contaId=?", (valor, conta_id))
            conexao.commit()
        else:
            print("Valor Inválido!")
    
    def sacar(self,conta_id, conexao, curso, valor):
        
        cursor.execute("SELECT saldo FROM conta WHERE contaId = ?", (conta_id,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("Conta não encontrada!")
            return

        saldo = resultado[0]

        if valor <= 0:
            print("Valor inválido!")
            return

        if saldo >= valor:
            # Atualiza saldo
            cursor.execute("UPDATE conta SET saldo = saldo - ? WHERE contaId=?", (valor, conta_id))
            
            # Registra transação
            cursor.execute("""
                INSERT INTO transacoes (id_conta_origem, tipo, valor, data)
                VALUES (?, ?, ?, DATE('now'))
            """, (contaId, "saque", valor))

            conexao.commit()
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente!")
