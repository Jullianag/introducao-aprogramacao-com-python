"""
3.13 - Escreva um programa que converta uma temperatura digitada
em °C em °F.
"""

temp_c = float(input('Digite a temperatura em °C: '))

F = (9 * temp_c) / 5 + 32

print(f'A temperatura {temp_c}°C corresponde a {F}°F')