
PIN = 150.40
PER = 170.20
MOG = 190.90
IPE = 210.10
IMB = 220.70

transRod = 1000
transFerr = 2000
transHidro = 2500

print("Bem-vindo à Madeireira do Cezar Isac Simeão Barbosa!")


def escolha_tipo():
    while True:
        tipo = input("""
Escolha o tipo de madeira:
PIN - Tora de Pinho
PER - Tora de Peroba
MOG - Tora de Mogno
IPE - Tora de Ipê
IMB - Tora de Imbuia
>> """).upper()

        if tipo == "PIN":
            return PIN, "Pinho"
        elif tipo == "PER":
            return PER, "Peroba"
        elif tipo == "MOG":
            return MOG, "Mogno"
        elif tipo == "IPE":
            return IPE, "Ipê"
        elif tipo == "IMB":
            return IMB, "Imbuia"
        else:
            print("Escolha inválida, entre com o modelo novamente")


def qtd_toras():
    while True:
        try:
            qtd = float(input("Digite a quantidade de toras (m³): "))

            if qtd <= 0:
                print("❌ Quantidade inválida.")
                continue

            if qtd < 100:
                desconto = 0
            elif qtd < 500:
                desconto = 0.04
            elif qtd < 1000:
                desconto = 0.09
            elif qtd <= 2000:
                desconto = 0.16
            else:

                print("Não aceitamos pedidos com essa quantidade de toras. Por favor, entre com a quantidade novamente.")
                continue

            return qtd, desconto

        except ValueError:
            print("Valor inválido! Digite apenas números.")


def transporte():
    while True:
        try:
            tipo = int(input("""
Escolha o tipo de transporte:
1 - Rodoviário (R$ 1000)
2 - Ferroviário (R$ 2000)
3 - Hidroviário (R$ 2500)
=> """))

            if tipo == 1:
                return transRod, "Rodoviário"
            elif tipo == 2:
                return transFerr, "Ferroviário"
            elif tipo == 3:
                return transHidro, "Hidroviário"
            else:
                print("❌ Opção inválida!")
        except ValueError:
            print("❌ Digite um número válido.")



try:
    valor_madeira, nome_madeira = escolha_tipo()
    qtd, desconto = qtd_toras()
    valor_transporte, nome_transporte = transporte()

    total = ((valor_madeira * qtd) * (1 - desconto)) + valor_transporte

    print(f"Total: R$ {total:.2f}")


except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

