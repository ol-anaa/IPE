'''
Faça um programa que leia um vetor A[100]. 
No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 
e o valor armazenado em cada uma das posições.
'''
list = []

for i in range(100):
    entrada = float(input())
    list.append(entrada)

for index, num in enumerate(list):
    if num <= 10:
        print(f"A[{index}] = {num}")