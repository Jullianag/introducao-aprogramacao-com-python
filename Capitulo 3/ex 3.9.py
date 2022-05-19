"""
3.9 - Escreva um programa que leia a quantidade de dias, horas, minutos e
segundos do usuário. Calcule o total em segundos.
"""

dias = int(input('Digite o número de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))

dia = 86400 * segundos
hora = 3600 * segundos
minutos = 60 * segundos
total = dia + hora + minutos + segundos

print(f'O total em segundos é: {total}')

