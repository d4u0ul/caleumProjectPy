import abc  # import de  abstratos
from abc import ABC
from excecoes import SaldoInsuficienteError

class Banco:
    pass


# classe abstrata
class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    #	outros	métodos	e	properties
    # metodo abstrato
    @abc.abstractmethod
    def get_bonificacao(self):
        return self._salario * 0.10


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciaveis = qtd_gerenciaveis

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000


class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        if (hasattr(obj, 'get_bonificacao')):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print(
                'instância	de	{}	não	implementa	o	método	get_bonificacao()'.format(
                    obj.__class__.__name__))

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes


class Cliente:
    def __init__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha


class Diretor(Funcionario):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

import datetime


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("data	abertura:	{}".format(self.data_abertura))
        print("transações:	")
        for t in self.transacoes:
            print("-", t)


class Autenticavel:
    def autentica(self, senha):
        pass


class Conta:
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self,valor):
        self._saldo = valor

    # código	omitido
    def deposita(self, valor):
        if (self.saldo < valor):
            raise ValueError("valor negativo")
        else:
            self.saldo +=valor
            self.historico.transacoes.append("depósito	de	{}".format(valor))

    def saca(self, valor):
        print("sacando")

        if (valor < 0):
            raise ValueError('Você	tentou	sacar	um	valor	negativo.')
        if (self._saldo < valor):
            raise SaldoInsuficienteError('Saldo	insuficiente.')
        else:
            self._saldo -= (valor + 0.10)
            self.historico.transacoes.append("saque	de	{}".format(valor))

    def extrato(self):
        print("numero:	{}	\nsaldo:	{}".format(self.numero, self.saldo))
        self.historico.transacoes.ap

    @abc.abstractmethod
    def atualiza(self, valor):
        pass


class ContaInvestimento(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        super().__init__(numero, titular, saldo=0, limite=1000.0)
        pass


# verifica	se	a	senha	confere


class ContaCorrente(Conta):
    def atualiza(self, valor):
        pass


class ContaPoupanca(Conta):
    # def atualiza(self, valor):
    #    pass
    pass


if __name__ == '__main__':
    # diretor = Diretor('joao', '111111111-11', 4000.0)
    ## funcionario = Funcionario('João', '111111111-11', 2000.0)
    ## print("bonificacao	funcionario:	{}".format(funcionario.get_bonificacao()))
    # gerente = Gerente("José", "222222222-22", 5000.0, '1234', 0)
    # print("bonificacao	gerente:	{}".format(gerente.get_bonificacao()))
    # controle = ControleDeBonificacoes()
    ## controle.registra(funcionario)
    # controle.registra(gerente)
    # print("total:	{}".format(controle.total_bonificacoes))
    # cliente = Cliente('Maria', '333333333-33', '1234')
    # controle = ControleDeBonificacoes()
    # controle.registra(cliente)
    ci = ContaInvestimento('123-6', 'Maria', 1000.0)
    cc = ContaCorrente('123-4', 'João', 1000.0)
    cp = ContaPoupanca('123-5', 'José', 1000.0)
    cc.atualiza(0.01)
    try:
        cc.saca(10000)
    except ValueError:
        print("valor err")
    except SaldoInsuficienteError:
        print ("Saldo insuficiente2")
    cp.atualiza(0.01)
    print(cc.saldo)
    print(cp.saldo)
