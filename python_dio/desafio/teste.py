# Recebe a entrada e armazena na variável "entrada"
entrada = input()


# Função reponsável por extrair os domínios dos emails
def extrair_dominios(emails):
    # Separa os emails por ponto e vírgula
    lista_emails = emails.split(";")
    usuario, dominio = emails.split("@")
    print(dominio)

extrair_dominios(entrada)