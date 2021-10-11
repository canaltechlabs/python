from os import system
system("clear")

f = open("file.txt", "r")

for x in f:
    print("Listar o diretorio {}".format(x))
    system("ls /{}".format(x))
    print(" ")

f.close()