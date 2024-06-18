class Bicicleta:
    def __init__(self, cor, modelo,ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim.....")
    
    def parar(self):
      print('Parando')
      print('Bicicleta Parada')

    def correr(self):
        print("Vrummm....")  
    
    def get_cor(self):
        return self.cor
    
    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
b2 = Bicicleta("Verde", 'Monark', 2024, 1200)


b1.correr()  #Bicicleta.correr(b1)
b1.buzinar() #Bicicleta.buzinar(b1) 
b1.parar()   #Bicicleta.parar(b1)

print("-"*30)

print(b1)

