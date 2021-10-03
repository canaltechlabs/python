# O Básico de Python com um Jogo

Quero com uma lógica de comparações fazer condicionais e laços de repetições

Bora, seguir!!!

## Limpando a tela na hora da execução

Para ficar mais apresentável o código eu uso o comando clear do Sistema Operacional para executar o script.

Com isso mostro um exemplo simples de importação de módulo e função especifica que vou usar.

```python
from os import system 
system("clear")
```

## Defindo váriaveis

Vamos definir duas variáveis e começar

```python
nome = "Renato"
idade = 37

print("#" * 45)
print("# Vamos adivinhar a idade do {}? #".format(nome))
print("#" * 45)

palpite = input("Digite seu palpite sobre a idade: ")
```

## Primeira condição com if

Vamos agora fazer uma condição para saber se o número digitado corresponde com a idade

```python
if (idade == palpite):
    print("Você acertou!")
else:
    print("Você errou!")
```

Vamos testar o código e vemos que quando digitamos 37, que é a idade ele mostra uma mensagem que você errou, Porque isso aconteceu?

Isso, aconteceu porque sempre que você usa a função input ele é uma string, compare antes do if para ver

**Obs: Isso no Python 3**

```python
print(type(idade))
print(type(palpite))
```

Vamos corrigir isso para que o palpite de 37 seja igual a variável idade do nosso código.

```python
if (idade == int(palpite)):
    print("Você acertou!")
else:
    print("Você errou!")
```

## Usando elif "Se não, se..."

Este software termina muito rápido e precisamos dar uma dica para o usuário se este chute foi abaixo ou acima, vamos ajudar o usuário a chegar mais próximo da idade?

```python
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
```

Aqui nós, convertemos o palpite em um número inteiro e depois comparamos se ele digitou um número maior, menor ou igual. E adicionamos uma mensagem de fim de jogo.

## Programa só termina quando acertar

Agora, vamos usar a lógica do laço while, para que o programa só termine quando acertar a idade, vimos que já temos a dica de quando o valor é menor ou maior então a gente consegue chegar mais facilmente no valor correto da idade.

Vamos importa a biblioteca "time", para usar a função sleep pro nosso código ficar bem legal.

```python
import time
```

Depois criaremos um laço while em nosso código

```python
while (igual != True):
```

Para que a gent consiga ver o que está acontecendo adicionaremos um sleep e limpamos a tela para fazer uma nova tentativa.

```python
time.sleep(3)
system("clear")
```

Deixe o print fora do laço para mostrar que o jogo terminou

```python
print("Parabéns e fim de jogo!")
```

Aqui aprendemos de uma forma simples a usar o laço while.

Agora o código completo fica assim:

```python
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

print("Parabéns e fim de jogo!")
```
