def main():
    contador = int(input("Quantas Horas extras foram feitas no final de semana? "))

    Salario = 1824.36
    hn = 9.01  # valor da hora normal (não usado nesse cálculo, mas deixei caso precise)
    he = 28  # valor da hora extra

    def calculaExtra(he, contador):
        heTotal = contador * he
        SalarioTotal = Salario + heTotal
        Adiantamento = 793.2
        SalarioQuinto = SalarioTotal - Adiantamento
        print(f"Você vai receber dia 20: R$ {Adiantamento:.2f}, e dia 5: R$ {SalarioQuinto:.2f}, totalizando: R$ {SalarioTotal:.2f}")

    calculaExtra(he, contador)

main()
