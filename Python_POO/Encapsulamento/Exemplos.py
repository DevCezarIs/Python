class Conta:
    def __init__(self, saldo = 0):
        self._saldo = saldo
        
    def deposito(self, saldo):
        print("Quanto deseja depositar?")
        print(f"Ok seu saldo agora é {saldo}")

    def saque(self, saldo):
        if saldo <= 0:
            print("Ops, Deposite alguma quantia antes de realizar um saque!")

        else:
            print("Quanto desseja sacar?")
            saque_request = input()

            if saque_request > saldo:
                print("Ops, Deposite alguma quantia maior antes de realizar esse saque")
    
    def extrato(self, saldo):
        print(f"Seu saldo agora é de R$ {saldo}")


Cezar = Conta(0)

Cezar.saque(0)
Cezar.deposito(input("Qual valor?"))
Cezar.saque(input("Qual valor?"))
Cezar.extrato(input("Qual valor?"))
