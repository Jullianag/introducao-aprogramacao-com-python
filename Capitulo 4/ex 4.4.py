"""
4.4 - Escreva um programa que permite que pergunte o salário do funcionário e calcule
o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, de 15%
"""

salario = float(input('Digite o seu salario: '))

if salario > 1250:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f'Salario com aumento de 10% é: R$ {novo_salario}')
else:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f'Salario com aumento de 15% é: R$ {novo_salario}')