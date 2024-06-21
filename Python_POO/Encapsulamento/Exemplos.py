class Conta:
    def __init__(self, saldo=0):
        self.__saldo = saldo

    def deposito(self, valor):
        self.__saldo += valor
        print(f"Ok, seu saldo agora é R$ {self._saldo:.2f}")

    def saque(self, valor):
        if self.__saldo <= 0:
            print("Ops, depósita alguma quantia antes de realizar um saque!")
        elif valor > self.__saldo:
            print("Ops, saldo insuficiente para realizar esse saque!")
        else:
            self.__saldo -= valor
            print(f"Ok, seu saldo agora é R$ {self.__saldo:.2f}")

    def extrato(self):
        print(f"Seu saldo agora é de R$ {self.__saldo:.2f}")


# Criar uma conta com saldo inicial de 0
Cezar = Conta(0)

# Realizar operações na conta
Cezar.saque(0)
valor_deposito = float(input("Qual valor para depósito? "))
Cezar.deposito(valor_deposito)
valor_saque = float(input("Qual valor para saque? "))
Cezar.saque(valor_saque)
Cezar.extrato()
