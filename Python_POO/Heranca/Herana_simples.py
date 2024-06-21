class veiuculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando Motor")

class motocicleta(veiuculo):
    pass


class carro(veiuculo):
    pass
 

class Caminhao(veiuculo):
    def esta_carregado(self):
        print("Ainda não")


motocicleta = motocicleta("Preta", "ABC-157", 2)
motocicleta.ligar_motor()

carro = carro("Cinza", "CDE-164", 4)
carro.ligar_motor()

Caminhao = Caminhao("Roxo", "CMN-365",)
Caminhao.ligar_motor()