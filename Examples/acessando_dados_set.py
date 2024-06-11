'''Para acessar dados no set é necessario transformá-los 
para uma lista para assim podermos acessar os elementos '''

numeros = {1, 2, 3, 4}
# print(numeros[0]) #Erro
numeros = list(numeros)
print(numeros[0])#agora sim
