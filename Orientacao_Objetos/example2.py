class cofre:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
    
    def exibir(self):
        print(f'Cofre de {self.nome}\nSaldo: {self.saldo}')
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return True

    def sacar(self, valor):
        if (self.saldo - valor) < 0:
            print('Saldo Insuficiente!')
            return False
        self.saldo = self.saldo - valor
        return True
    
    def verificaSaldo(self):
        return self.saldo


cofre1 = cofre('Renato',100.00)
cofre2 = cofre('Juca',65.00)

print(cofre1.__dict__)
print(cofre2.__dict__)

cofre1.exibir()

cofre1.depositar(50.01)
print(cofre1.saldo)

print(f'Depositar 50: {cofre1.depositar(50)}')
print(f'Saldo: {cofre1.verificaSaldo()}')
print(f'Sacar 50: {cofre1.sacar(50)}')
print(f'Saldo: {cofre1.verificaSaldo()}')

print(f'Sacar 500: {cofre1.sacar(500)}')
print(f'Saldo novamente: {cofre1.verificaSaldo()}')

