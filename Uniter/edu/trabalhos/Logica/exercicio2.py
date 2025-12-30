print("""
----------Bem Vindo à Pizzaria do Cezar Isac-----------------
----------------------Cardápio-------------------------------
-------------------------------------------------------------
---| Tamanho  |  Pizza Salgada (PS)  |  Pizza Doce (PD)  |---
---|    P     |      R$ 30,00        |     R$ 34,00      |---
---|    M     |      R$ 45,00        |     R$ 48,00      |---
---|    G     |      R$ 60,00        |     R$ 66,00      |---
-------------------------------------------------------------
""")

total = 0

while True:
    saborPizza = input("Entre com o sabor desejado (PS/PD): ").upper()
    if saborPizza not in ["PS", "PD"]:
        print("Sabor inválido. Tente novamente.")
        continue

    tamanhoPizza = input("Entre com o tamanho de Pizza desejado (P/M/G): ").upper()
    if tamanhoPizza not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente.")
        continue

    # Dicionário de preços
    Valor = {
        "PS": {"P": 30, "M": 45, "G": 60},
        "PD": {"P": 34, "M": 48, "G": 66}
    }

    ValorPedido = Valor[saborPizza][tamanhoPizza]
    total += ValorPedido

    print(f"Você pediu uma pizza {'Salgada' if saborPizza=='PS' else 'Doce'} tamanho {tamanhoPizza}: R$ {ValorPedido:.2f}")

    manter = input("Deseja continuar pedindo? (S/N): ").upper()
    if manter == "N":
        break

print(f"\nO valor total a ser pago é: R$ {total:.2f}")
