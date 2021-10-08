from os import system
import time
system("clear")

nome = "Renato"
idade = 37
igual = 0

while (igual != True):
    time.sleep(3)
    system("clear")
    print("#" * 39)
    print("# Vamos adivinhar a idade do {} ? #".format(nome))
    print("#" * 39)

    palpite = input("Digite seu palpite sobre a idade: ")

    palpite = int(palpite)
    igual = palpite == idade
    maior = palpite > idade
    menor = palpite < idade

    if (igual):
        print("Você acertou")
    elif (maior):
        print("O número é maior que a idade!")
    elif (menor):
        print("O número é menor que a idade!")

print("Parabéns, você acertou a idade!")