from os import system
import time
system("clear")

option=0

while (option != 3):
    time.sleep(3)
    system("clear")
    print("#" * 20)
    print("# Menu de opções #")
    print("# 1 - Opção 1    #")
    print("# 2 - Opção 2    #")
    print("# 3 - Sair       #")
    print("#" * 20)

    option = int(input("Digite sua opção: "))

    if (option == 1):
        print("Você escolheu a opção 1")
    elif (option == 2):
        print("Você escolheu a opção 2")
    elif (option == 3):
        print("Você escolheu sair")
    else:
        print("Opção inválida!, Escolha outra opção")

