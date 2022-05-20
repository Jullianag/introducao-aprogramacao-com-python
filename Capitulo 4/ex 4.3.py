"""
4.3 - Escreva um programa que leia três números e que imprima o maior e o menor.
"""

num1 = int(input('Escreva o primeiro número: '))
num2 = int(input('Escreva o segundo número: '))
num3 = int(input('Escreva o terceiro número: '))

if num1 > num2 and num1 > num3:
    print(f'Maior: {num1}')
elif num2 > num1 and num2 > num3:
    print(f'Maior: {num2}')
elif num3 > num1 and num3 > num2:
    print(f'Maior: {num3}')
