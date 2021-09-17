class Cliente:
    def __init__(self,nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.contato = None

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def contato(self):
        return self.__contato

    @Contato.setter
    def contato(self, contato):
        self.__contato = contato

class Email:
    def __init__(self, email):
        self.__email = email

    @property
    def email(self):
        return self.__email

    def ver(self):
        print(f'Contato: {self.__email}')


class Fone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def ver(self):
        print(f'Contato: ({self.ddd}) {self.numero}')

    