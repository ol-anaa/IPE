'''
Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, 
coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim 
sucessivamente. Mostre o vetor em seguida.
'''

entrada = int(input())
list = []

list.append(entrada)

for i in range(9):
    num = list[i]
    list.append(num * 2)

for index, item in enumerate(list):
    print(f"N[{index}] = {item}")

