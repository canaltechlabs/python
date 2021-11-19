from random import randint

class conta:
    def __init__(self,numero, digito, agencia, saldo):
        self.numero = numero
        self.digito = digito
        self.agencia = agencia
        self._saldo = saldo
# Objeto protegido self._saldo, tem que ficar assim no código todo

@staticmethod
def gerarNumero():
    num = randint(1000, 1999)
    return num

# Getter
@property
def saldo(self):
    return self.saldo
#Setter
@saldo.setter
def saldo(self, valor):
    if isinstance(valor, str):
        print('Saldo, deve ser numérico, saldo 0')
        self._saldo = 0
        return
    self._saldo = valor

# Gerar um número aleatório
print(cofre.gerarNumero())
conta3 = conta(conta.gerarNumero(), 0, 1010, 5000)

# Getter e Setter
conta4 = conta(conta.gerarNumero(), 0, 1010, 'R$500')
# Ordem no caos, para não deixar isso acontecer usamos getrer e setter
# Não permite criar bobagens na hora de construir o objeto



