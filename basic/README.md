# O básico de Python

Comecei a estudar Python e pretendo guardar meus códigos Python neste repositório.

# Primeiros contatos com Python

No Python para exibirmos algo na tela fazemos de forma bem simples

```python
print("Olá, mundo")
```

Recebendo uma valor em uma variável e exibindo

```python
nome = "Renato"
print(nome)
```

Usando concatenação de forma mais elegante

```python
print(nome + " é um desenvolvedor!")

print("Seu nome é:",nome)

print("Seu nome é: {}".format(nome))

print(f'Seu nome é: {nome})
```

Recebendo o nome de um usuário

```python
nome = input("Digite seu nome: ")
```

Um software que recebe o nome e sobre nome e exibe na tela

```python
print("Seu nome completo")
nome = input("Digite seu primeiro nome: ")
sob renome = input("Digite seu sobre nome: ")
nome_completo = nome + " " + sobrenome
print(sobrenome)
```

Mostrando o tipo da variável

```python
print(type(nome))
````

# Python não é fortemente tipado

Diferente de algumas linguagens o Python não é fortemente tipado ou seja, não definimos o tipo de variável, o tipo de variável é definido na hora da atribuição

```python   
numero = 10
print(type(numero))

numero = 10.5
print(type(numero))

numero = "texto"
print(type(numero))
```

# Operações matematicas com Python

Todo o valor que vem do input é uma string por padrão

```python
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

soma = num1 + num2
print("A operação é: " + soma)

print(type(num1))
print(type(num2))
```

Para realizar as operações é necessário converter em números e fazer uma leve mudança no print

```python
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

soma = float(num1) + float(num2)
print("A operação é: {}".format(soma))
```


