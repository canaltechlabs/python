from os import system
import time
system("clear")

count=1

while (count != 5):
    time.sleep(1)
    print("Você está na {} vez!".format(count))
    count=count+1
