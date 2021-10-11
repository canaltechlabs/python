from os import system
system("clear")
system("ls -l ~/projects/ | grep -v total | awk '{print $9}' > lista.txt")
arquivo = open("lista.txt", "r")

for linha in arquivo:
    print("atualizar o repo: {}".format(linha))
    system("cd /{} && git pull /{} && cd ..".format(linha,linha))
    print(" ")

arquivo.close()