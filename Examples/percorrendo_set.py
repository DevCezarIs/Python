#Sets são inacessiiveis mas podemos percorre-los com o for:
carros = {"gol", 'celta', 'palio', "porshe"}

for x in carros:
    print(x)

#Utilizando a Função Enumerate 

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')