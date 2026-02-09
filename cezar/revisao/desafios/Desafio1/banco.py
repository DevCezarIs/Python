class PessoaFisica:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta(PessoaFisica):
    def __init__(self, id, cliente, historico):
        super().__init__(cliente.nome, cliente.data_nascimento, cliente.cpf, cliente.endereco)
        self._saldo = 0
        self._id = id
        self._agencia = "0001"
        self._historico = historico()

    @classmethod
    def nova_conta(cls, cliente, id, historico):
        return cls(id, cliente, historico)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._id


    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self

    @property
    def historico(self):
        return self._historico