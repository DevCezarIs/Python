matriz =  [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[2][0])

numeros = [1 , 20 ,30 ,55 , 40 ,2 ,60 ,5]
numero = [numero for numero in numeros if numero % 2 ==0 ]

print(numero)

quadrado  = [quadrado ** 2 for quadrado in numeros]
print(quadrado)