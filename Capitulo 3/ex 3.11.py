"""
3.11 - Faça um programa que solicite o preço de uma mercadoria e o
percentual de desconto. Exiba o valor do desconto e o preço a pagar.
"""

valor = float(input('Digite o valor da mercadoria: '))
desconto = int(input('Valor do desconto em %: '))

valor_do_desconto = valor * desconto / 100
novo_valor = valor - valor_do_desconto

print(f'Valor do desconto: R$ {valor_do_desconto}\n'
      f'Preço a pagar: R$ {novo_valor}')

