"""
3.10 - Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário.
"""

salario = float(input("Digite o valor do seu salário: "))
aumento = int(input('Digite o valor do aumento em %: '))

valor_do_aumento = salario * aumento / 100

novo_salario = salario + valor_do_aumento

print(f'Foi solicitade um aumento de - {aumento}%  - correspondendo a: R$ {valor_do_aumento}')
print(f'O novo salario é de: R$ {novo_salario}')