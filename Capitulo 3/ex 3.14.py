"""
3.14 - Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa
R$ 60 por dia e RS 0,15 por km rodado.
"""

km = int(input('Digite a quantidade de km rodados: '))
dias = int(input('Digite a quantidade de dias alugados: '))

km_rodados = km * 0.15
dias_alugados = dias * 60
total = km_rodados + dias_alugados

print(f'Você alugou o carro por {dias} dias e rodou {km} km\n'
      f'Valor a pagar: R$ {total:.2f}')