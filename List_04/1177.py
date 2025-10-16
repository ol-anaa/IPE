''' 
Faça um programa que leia um valor T e preencha um vetor N[1000] 
com a sequência de valores de 0 até T-1 repetidas vezes, conforme exemplo abaixo. Imprima o vetor N.
'''

entrada = int(input())
count = 0

for i in range(1000):
    if count >= entrada:
        count = 0
    
    print(f"N[{i}] = {count}")
    count+=1