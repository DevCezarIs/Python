import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "BankSys.db")
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()


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
    def __init__(self, conta_id, nome, tel, data_cadastro):
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

    def deposito(self, cursor, conta_id, conexao, valor):
        if valor > 0:
            cursor.execute(
                "UPDATE conta SET saldo = saldo + ? WHERE contaId=?", (valor, conta_id)
            )
            conexao.commit()
            print(f"Depósito de R${valor:.2f} realizado!")
        else:
            print("Valor inválido!")

    def sacar(self, cursor, conta_id, conexao, valor):
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
            cursor.execute(
                "UPDATE conta SET saldo = saldo - ? WHERE contaId=?", (valor, conta_id)
            )
            cursor.execute(
                """
                INSERT INTO transacoes (id_conta_origem, id_conta_destino, tipo, valor, data)
                VALUES (?, NULL, ?, ?, DATE('now'))
            """,
                (conta_id, "saque", valor),
            )
            conexao.commit()
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente!")


def transferencia(cursor, conexao, conta_id_origem, conta_id_destino, valor):
    # Buscar saldo da conta de origem
    cursor.execute("SELECT saldo FROM conta WHERE contaId=?", (conta_id_origem,))
    resultado = cursor.fetchone()

    if resultado is None:
        print("Conta de origem não encontrada")
        return

    saldo_origem = resultado[0]

    if saldo_origem < valor:
        print("Saldo insuficiente")
        return

    # Deduzir valor da conta de origem
    cursor.execute(
        "UPDATE conta SET saldo = saldo - ? WHERE contaId=?", (valor, conta_id_origem)
    )

    # Adicionar valor à conta de destino
    cursor.execute("SELECT saldo FROM conta WHERE contaId=?", (conta_id_destino,))
    if cursor.fetchone() is None:
        print("Conta de destino não encontrada")
        conexao.rollback()
        return

    cursor.execute(
        "UPDATE conta SET saldo = saldo + ? WHERE contaId=?", (valor, conta_id_destino)
    )

    # Registrar transação
    cursor.execute(
        """
        INSERT INTO transacoes (id_conta_origem, id_conta_destino, tipo, valor, data)
        VALUES (?, ?, ?, ?, DATE('now'))
    """,
        (conta_id_origem, conta_id_destino, "transferencia", valor),
    )

    conexao.commit()
    print("Transferência realizada com sucesso!")
