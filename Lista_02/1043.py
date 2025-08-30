'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo.
Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C 
como altura, mostrando a mensagem
Area = XX.X
'''
entrada = input()
A, B, C = entrada.split()

A = float(A)
B = float(B)
C = float(C)

if C < (A + B) and B < (A + C) and A < (B + C):
    per = A + B + C
    print(f"Perimetro = {per:.1f}")
else:
    ar = ((A + B) * C) /2
    print(f"Area = {ar:.1f}")