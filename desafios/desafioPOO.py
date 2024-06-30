class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        
    def verificar_saldo(self):
        if self.saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
        
    def mensagem_personalizada(self):
        return self.verificar_saldo()


class UsuarioTelefone:
    def __init__(self, nome, plano, saldo):
        self.nome = nome
        self.plano = PlanoTelefone(plano, saldo)
        
    def verificar_saldo(self):
        return self.plano.verificar_saldo()
    
    def mensagem_personalizada(self):
        return self.plano.mensagem_personalizada()


# Exemplo de uso
def main():
    nome = input()
    plano = input()
    saldo = int(input())

    usuario = UsuarioTelefone(nome, plano, saldo)
    print(usuario.mensagem_personalizada())


if __name__ == "__main__":
    main()
