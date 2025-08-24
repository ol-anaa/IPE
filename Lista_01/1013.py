'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido 
da mensagem “eh o maior”. Utilize a fórmula matemática da distância entre dois pontos  no 
plano cartesiano.
'''
entrada = input()
a, b, c = entrada.split()

a = int(a)
b = int(b)
c = int(c)

MaiorAB = (a + b + abs(a-b))/2
result = (MaiorAB + c + abs(MaiorAB-c))/2

print(f"{result:.0f} eh o maior")