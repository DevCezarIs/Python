class Pessoa:
    def __init__(self, Rg, Cpf):
        self.rg = Rg
        self.cpf = Cpf
        
class Aluno(Pessoa):
    def __init__(self, inscricao = int, nota= float, presenca = float):
        self.incricao = inscricao
        self.nota = nota
        self.presenca = presenca

    def retencao(self):
        if self.nota < 7 and self.presenca < 75:
            print("Reprovado")
        
        else:
            print("Aprovado")

Cezar = Aluno(555, 9, 100.0)
Cezar.retencao()