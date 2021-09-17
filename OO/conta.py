class conta:
    def __init__(self,numero, digito, agencia, saldo):
        self.numero = numero
        self.digito = digito
        self.agencia = agencia
        self.saldo = saldo
    
    def dadosConta(self):
        print(f'Agencia: {self.agencia} - cc:{self.numero}/{self.digito} - saldo:{self.saldo}')

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return True
    
    def sacar(self, valor):
        if (self.saldo - valor) < 0:
            print("Saldo insuficiente :(")
            return False
        self.saldo = self.saldo - valor
        return True

    def verificarSaldo(self):
        return self.saldo

print("Abrindo uma conta")

conta1 = conta(100, 1, 1010, 50.01)
conta2 = conta(200, 2, 1010, 500)

conta1.dadosConta()
conta2.dadosConta()

print(f'Deposito 100: {conta1.depositar(100)}')
print(f'Saldo: {conta1.verificarSaldo()}')
print(f'Sacar 50.01 {conta1.sacar(50.01)}')
print(f'Saldo: {conta1.verificarSaldo()}')
print(f'Sacar 500 {conta1.sacar(500)}')

print(f'Saldo sem alteração {conta1.verificarSaldo()}')

