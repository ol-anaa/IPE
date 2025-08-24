'''
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, 
o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número
e o salário do funcionário, com duas casas decimais.
'''
NUM = int(input())
HRSTRAB = int(input())
VAL = float(input())

RESULT = VAL * HRSTRAB

print(f"NUMBER = {NUM}")
print(f"SALARY = U$ {RESULT:.2f}")
