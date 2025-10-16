''' 
Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. 
Lembre que os 2 primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele. 
Todos os valores de Fibonacci calculados neste problema devem caber em um inteiro de 64 bits sem sinal.
'''

casos = int(input())
list = []
fibonacci = [0, 1]

for i in range(2, 61):
    fibonacci.append((fibonacci[i - 1]) + (fibonacci[i - 2]))

for _ in range(casos):
    n = int(input())
    list.append(f"Fib({n}) = {fibonacci[n]}")

for i in list:
    print(i)

