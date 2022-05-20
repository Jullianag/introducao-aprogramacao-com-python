"""
3.15 - Escreva um programa para calcular a redução do tempo de vida de
um fumante. Pergunte a quantidade de cigarros fumados por dia e quantis anos
ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""

cigarros_fumados = int(input('Digite a quantidade de cigarros fumados por dia: '))
anos = int(input('Digite a quantidade de anos que você já fumou: '))

minutos_de_vida = cigarros_fumados * 10

dias_ja_fumados = anos * 365



