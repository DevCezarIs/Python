class UsuarioTelefone:
    def __init__(self, nome, numero, saldo):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
    
    def fazer_chamada(self, destino, duracao):
        custo = duracao * 0.10
        if self.saldo < custo:
            print("Saldo insuficiente para fazer a chamada.")
        else:
            self.saldo -= custo
            print(f"Chamada para {destino} realizada com sucesso. Saldo atual: ${self.saldo:.2f}")

    def verificar_saldo(self):
        return f"Saldo atual: ${self.saldo:.2f}"


def main():
    nome = input("Digite seu nome: ")
    numero = input("Digite seu número: ")
    saldo = float(input("Digite seu saldo inicial: "))
    destino = input("Digite o destino da chamada: ")
    duracao = float(input("Digite a duração da chamada em minutos: "))

    usuario = UsuarioTelefone(nome, numero, saldo)
    usuario.fazer_chamada(destino, duracao)
    print(usuario.verificar_saldo())


if __name__ == "__main__":
    main()
