class filme:
    def __init__(self, nome, genero, ano, duracao):
        self.nome = nome
        self.genero = genero
        self.ano = ano
        self.duracao = duracao

print('#'*30)
print ("Vamos usar uma classe!")
shrek = filme('Shrek', 'comedia', '2001', '94min')
avatar = filme('avatar', 'aventura', '2009', '162min') 
print('#'*30)

print("O filme {} tem as seguintes caracteristicas:".format(shrek.nome))
print("Gênero: {}".format(shrek.genero))
print("Ano: {}".format(shrek.ano))
print("Duração: {}".format(shrek.duracao))

print('#'*30)
print(f'O filme {avatar.nome} é do gênero {avatar.genero} foi lançado em {avatar.ano} e tem duração de {avatar.duracao}')

print(f"Conteúdo do Objetos {avatar.__dict__}") 
print(f"Conteúdo do Objetos {shrek.__dict__}") 