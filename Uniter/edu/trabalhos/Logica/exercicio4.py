
print("Bem-vindo à Lista de Contatos do Cezar Isac")
print("--------------------------------------------------")

lista_contatos = []  # Lista de dicionários
id_global = 5013355  # Exemplo de RU

def cadastrar_contato(id):
    print("\n----------- MENU CADASTRAR CONTATO -----------------")
    print(f"Id do Contato: {id}")

    nome = input("Por favor entre com o nome do Contato: ")
    atividade = input("Por favor entre com a Atividade do contato: ")
    telefone = input("Por favor entre com o telefone do contato: ")

    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }

    lista_contatos.append(contato.copy())
    print("--------------------------------------------------")
    print(f"Contato '{nome}' cadastrado com sucesso!\n")

def consultar_contatos():
    while True:
        print("""
        ---- MENU CONSULTA ----
        1. Consultar Todos
        2. Consultar por Id
        3. Consultar por Atividade
        4. Retornar ao Menu Principal
        ------------------------
        """)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if len(lista_contatos) == 0:
                print("Nenhum contato cadastrado.")
            else:
                print("\n--- Lista Completa de Contatos ---")
                for c in lista_contatos:
                    print(f"ID: {c['id']}\n Nome: {c['nome']}\n "
                          f"Atividade: {c['atividade']}\n Telefone: {c['telefone']}\n")
                print("-----------------------------------")

        elif opcao == "2":
            try:
                id_busca = int(input("Digite o ID do contato: "))
                encontrado = False
                for c in lista_contatos:
                    if c["id"] == id_busca:
                        print(f"ID: {c['id']}\n Nome: {c['nome']}\n "
                          f"Atividade: {c['atividade']}\n Telefone: {c['telefone']}\n")
                        encontrado = True
                        break
                if not encontrado:
                    print("ID não encontrado.")
            except ValueError:
                print("Digite um número válido para o ID.")

        elif opcao == "3":
            atividade_busca = input("Digite a atividade: ").lower()
            encontrados = [c for c in lista_contatos if c["atividade"].lower() == atividade_busca]

            if len(encontrados) == 0:
                print("Nenhum contato encontrado com essa atividade.")
            else:
                print(f"\nContatos com a atividade '{atividade_busca}':")
                for c in encontrados:
                   print(f"ID: {c['id']}\n Nome: {c['nome']}\n "
                          f"Atividade: {c['atividade']}\n Telefone: {c['telefone']}\n")

        elif opcao == "4":
            return
        else:
            print("Opção inválida! Tente novamente.")

def remover_contato():
    while True:
        try:
            id_remover = int(input("Digite o ID do contato que deseja remover: "))
            for c in lista_contatos:
                if c["id"] == id_remover:
                    lista_contatos.remove(c)
                    print(f"Contato de ID {id_remover} removido com sucesso!\n")
                    return
            print("Id inválido! Tente novamente.")
        except ValueError:
            print("Digite um número válido para o ID.")

while True:
    print("""
    ----------------- MENU PRINCIPAL -----------------
    Escolha a opção desejada:
    1 - Cadastrar Contato
    2 - Consultar Contato(s)
    3 - Remover Contato
    4 - Sair
    --------------------------------------------------
    """)
    opcao = input(">> ")

    if opcao == "1":
        cadastrar_contato(id_global)
        id_global += 1  # Incrementa o ID a cada novo cadastro
    elif opcao == "2":
        consultar_contatos()
    elif opcao == "3":
        remover_contato()
    elif opcao == "4":
        print("Programa encerrado. Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")


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

