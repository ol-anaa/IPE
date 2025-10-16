'''
Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.
'''
list = []

for i in range(10):
    entrada = int(input())

    if entrada <= 0:
        entrada = 1

    list.append(entrada)

for index, item in enumerate(list): 
    print(f"X[{index}] = {item}")
