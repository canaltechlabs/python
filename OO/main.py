from classes import Cliente, Email, Fone

# Objeto Cliente

print('===== Clientes ===')
cli1 = Cliente('Pedro','123.123.123')

print(cli1.__dict__)

cli1_email = Email('jose@fiap.edu.br')
cli1_email.ver()
cli1_fone = Fone('11', '98123485')


print(cli1)
print(cli1_email)
print(cli1_fone)
