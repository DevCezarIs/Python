limiteSaque = 500
saldo = 0
cont_Saques = 3
extrato = ""
saque = 0

while True:
    print(
        f'''
                Banco v0.1

            O que deseja fazer?

        (d) Depósito    (e)Extrato
        (s) Saque       (q)Sair

Saldo: R$ {saldo:.2f}   limite de saques: {cont_Saques}
    
        '''
    )
    opcao = input("Digite aqui: ").lower().strip()

    if opcao == "d":
        deposito = float(input("Qual valor será depositado? "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "s":
        if cont_Saques > 0:
            saque = float(input("Qual valor será sacado? "))
            if saque > 0 and saque <= limiteSaque and saque <= saldo:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                cont_Saques -= 1
            else:
                print("Operação falhou! O valor do saque é inválido ou excede o saldo/limite.")
        else:
            print("Operação falhou! Você atingiu o limite de saques.")

    elif opcao == "e":
        print("\nExtrato:")
        print(extrato if extrato else "Não há movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Saindo do Banco...")
        break

    else:
        print("Opção inválida, por favor selecione novamente.")
