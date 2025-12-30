"""
Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app para uma empresa X que vende Planos de Saúde. Uma das estratégias dessa empresa X é cobrar um valor diferente com base na idade do cliente, conforme a listagem abaixo:

· Se a idade for maior ou igual que 0 e menor que 19, o valor será de 100% do valor base do plano (100 / 100);

· Se a idade for maior ou igual que 19 e menor que 29, o valor será de 150% do valor base do plano (150 / 100);

· Se a idade for maior ou igual que 29 e menor que 39, o valor será de 225% do valor base do plano (225 / 100);

· Se a idade for maior ou igual que 39 e menor que 49, o valor será de 240% do valor base do plano (240 / 100);

· Se a idade for maior ou igual que 49 e menor que 59, o valor será de 350% do valor base do plano (350 / 100);

· Se a idade for maior ou igual que 59, o valor será de 600% do valor base do plano (600 / 100);
"""

print("Bem-vindo ao Sistema do Cezar Isac")

valorBase = float(input("Informe o valor base do plano: R$ "))
idade = int(input("Informe a idade do cliente: "))

#Funcao que retorna a porcetagem com base na idade 
def CalculaPorcentagem(idade):
    if idade < 0:
        print("Idade Inválida")
        return None
    elif idade < 19:
        return 1.0
    elif idade < 29:
        return 1.5
    elif idade < 39:
        return 2.25
    elif idade < 49:
        return 2.4
    elif idade < 59:
        return 3.5
    else:
        return 6.0

porcentagem = CalculaPorcentagem(idade)

valor_plano = valorBase * porcentagem #Calcula o valor do plano chamando a funcao criada acima 
print(f"O valor mensal do plano é de R$ {valor_plano:.2f}")


