'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. 
Em seguida, calcule e mostre:

a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
'''

entrada = input()
A, B, C = entrada.split()

A = float(A)
B = float(B)
C = float(C)

#Area do triângulo retângulo 
AreaTri = (A * C)/2

#Area do círculo
pi = 3.14159
AreaCir = (C ** 2) * pi

#Area do trapézio
AreaTra = ((A + B) * C)/2

#Area do quadrado 
AreaQua = B * B

#Area do retângulo  
AreaRet = A * B

print(f"TRIANGULO: {AreaTri:.3f}")
print(f"CIRCULO: {AreaCir:.3f}")
print(f"TRAPEZIO: {AreaTra:.3f}")
print(f"QUADRADO: {AreaQua:.3f}")
print(f"RETANGULO: {AreaRet:.3f}")