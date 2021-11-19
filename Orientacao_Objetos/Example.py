from os import system
system("clear")

class filme:
    def __init__(self, nome, genero, ano, duracao):
        self.nome = nome
        self.genero = genero
        self.ano = ano
        self.duracao = duracao

print('#'*26)
print ("# Vamos usar uma classe! #")
shrek = filme('shrek', 'comedia', '2001', '94min')
avatar = filme('avatar', 'aventura', '2009', '162min')
print('#'*26)

# print("O filme {} tem as seguintes caracteristicas:".format(shrek.nome))
# print("Gênero: {}".format(shrek.genero))
# print("Ano: {}".format(shrek.ano))
# print("Duração: {}".format(shrek.duracao))

# print('#'*30)
# print(f'O filme {avatar.nome} é do gênero {avatar.genero} foi lançado em {avatar.ano} e tem duração de {avatar.duracao}')

print(f"Conteúdo dos Objetos {avatar.__dict__}") 
print(f"Conteúdo dos Objetos {shrek.__dict__}") 