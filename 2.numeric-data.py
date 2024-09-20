def operacoes_basicas(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} x {num2} = {num1 * num2}")
    print(f"{num1} / {num2} = {num1 / num2}")

# Exemplo de uso
operacoes_basicas(4, 5)

# Solicitando a entrada e convertendo para um número inteiro
numero = int(input("Digite um número: "))

# Realizando o cálculo
calculo = numero + 20

# Imprimindo o resultado do cálculo
print(f"O resultado do cálculo é: {calculo}")

# Solicitando nome, sobrenome e idade
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = input("Digite sua idade: ")

# Concatenando nome, sobrenome e idade com espaços e exibindo
print(f"{nome} {sobrenome}, {idade} anos")

# Definindo as variáveis
numero = 10
numero_dois = 20
numero_dois += 30

# Verificando se 'numero' é menor que 'numero_dois'
if numero < numero_dois:
    # Imprimindo o resultado
    print(f"{numero} é menor que {numero_dois}")

print(1 + 1)   # Exemplo de adição
print(100 / 33) # Exemplo de divisão
print(2 ** 2)   # Exemplo de exponenciação

# Definindo a variável 'valor' com uma operação aritmética complexa
valor = (2 + 3) * 4 ** 2 / (2 - 1) - 5

# Imprimindo o valor da variável 'valor'
print(valor)

# Definindo a variável 'maca' com um valor inteiro
maca = 2

# Definindo a variável 'laranja' com um valor de string
laranja = "Laranja"

# Concatenando a string 'laranja' com o valor de 'maca' convertido para string
limoes = str(maca) + " " + laranja

# Imprimindo o valor da variável 'maca'
print(maca)

# Imprimindo o valor da variável 'limoes'
print(limoes)

# Definindo a variável 'maca' com um valor inteiro
maca = 2

# Definindo a variável 'laranja' com um valor de string
laranja = "Laranja"

try:
    # Tentando concatenar a string 'laranja' com o valor de 'maca' convertido para string
    limoes = str(maca) + " " + laranja
    # Imprimindo o valor da variável 'maca'
    print(maca)
    # Imprimindo o valor da variável 'limoes'
    print(limoes)
except TypeError as e:
    # Tratando o erro de tipo
    print(f"Ocorreu um erro de tipo: {e}")
except Exception as e:
    # Tratando qualquer outro tipo de erro
    print(f"Ocorreu um erro: {e}")

2 + 2

4 - 2

2 * 2

2 * 2

4 / 2

print("Python has three numeric types: int, float, and complex")

myValue = 1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue = 3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue = 1 + 2j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue = True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

"""Neste exemplo, a função imprimir_contas recebe uma lista de contas em formato de string, calcula o resultado de cada uma usando a função eval e imprime a conta junto com o resultado.

Se precisar de mais alguma coisa ou tiver outra dúvida, é só falar!
"""

# Lista de contas
contas = ["2 + 2", "4 - 2", "2 * 2", "2 * 2", "4 / 2"]

# Função para calcular e imprimir uma conta por vez
def imprimir_contas(contas):
    for conta in contas:
        resultado = eval(conta)
        print(f"{conta} = {resultado}")

# Chamar a função para imprimir as contas
imprimir_contas(contas)

print("Python has three numeric types: int, float, and complex")
myValue = 1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue = 3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue = 1 + 2j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue = True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

"""Esta linha imprime a mensagem “Python has three numeric types: int, float, and complex” na tela. É uma declaração informativa sobre os tipos numéricos em Python."""

print("Python has three numeric types: int, float, and complex")

"""Aqui, a variável myValue é definida com o valor inteiro 1."""

myValue = 1

"""

Esta linha imprime o valor da variável myValue, que é 1.

"""

print(myValue)

"""Esta linha imprime o tipo de dado da variável myValue, que é <class 'int'>, indicando que myValue é um inteiro."""

print(type(myValue))

"""Esta linha converte myValue e seu tipo de dado para strings e os concatena, resultando na impressão da mensagem “1 is of the data type <class ‘int’>”."""

print(str(myValue) + " is of the data type " + str(type(myValue)))

"""Aqui, myValue é redefinido com o valor 3.14, que é um número de ponto flutuante (float)."""

myValue = 3.14

"""Esta linha imprime o valor de myValue, que agora é 3.14."""

print(myValue)

"""Esta linha imprime o tipo de dado de myValue, que é <class 'float'>, indicando que myValue é um número de ponto flutuante."""

print(str(myValue) + " is of the data type " + str(type(myValue)))

"""Aqui, myValue é redefinido com o valor 1 + 2j, que é um número complexo."""

myValue = 1 + 2j

"""Esta linha imprime o valor de myValue, que agora é 1 + 2j."""

print(myValue)

"""Esta linha imprime o tipo de dado de myValue, que é <class 'complex'>, indicando que myValue é um número complexo."""

print(str(myValue) + " is of the data type " + str(type(myValue)))

"""Aqui, myValue é redefinido com o valor True, que é um valor booleano."""

myValue = True

"""Aqui, myValue é redefinido com o valor True, que é um valor booleano."""

print(myValue)

"""Esta linha imprime o tipo de dado de myValue, que é <class 'bool'>, indicando que myValue é um valor booleano."""

print(type(myValue))

"""Esta linha converte myValue e seu tipo de dado para strings e os concatena, resultando na impressão da mensagem “True is of the data type <class ‘bool’>”."""

print(str(myValue) + " is of the data type " + str(type(myValue)))
