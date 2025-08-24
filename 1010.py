'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário 
de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2.
Após, calcule e mostre o valor a ser pago.
'''

name = input()
sal = float(input())
vendas = float(input())

#15% de comissão sobre vendas ou 0.15
RESULT = sal + (vendas * 0.15)
print(f"TOTAL = R$ {RESULT:.2f}")