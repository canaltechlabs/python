# Limpar a tela
from os import system 
system("clear")

# Variáveis
nome = "Renato"
idade = 37

print("#" * 45)
print("# Vamos tentar adivinhar a idade do {}? #".format(nome))
print("#" * 45)

palpite = input("Digite seu palpite sobre a idade: ")
palpite = int(palpite)

igual = palpite == idade
maior = palpite > idade
menor = palpite < idade

if (igual):
    print("Você acertou!")
elif (maior):
    print("Você digitou um número maior!")
elif (menor):
    print("Você digitou um número menor!")

print("Fim de jogo!")
