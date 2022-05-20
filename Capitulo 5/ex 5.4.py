"""
5.4 - Modifique o programa anterior para imprimir de 1 ate o número
digitado pelo usuário, mas dessa vez, apenas os números ímpares.
"""

num = int(input('Digite o último número a imprimir: '))

x = 0
while x <= num:
    if x % 2 != 0:
        print(x)
    x += 1