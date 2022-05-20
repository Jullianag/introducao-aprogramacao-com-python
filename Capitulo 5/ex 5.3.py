"""
5.3 - Faça um programa para escrever a contagem regressiva do lançamento
de um foguete. O programa deve imprimir 10,9,8,...,1,0 e Fogo!
"""

from time import sleep


x = 10
while x >= 0:
    print(x, sep=' ')
    sleep(1)
    x -= 1

print('Fogo!')