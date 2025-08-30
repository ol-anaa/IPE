'''
Leia 2 valores com uma casa decimal (x e y), que devem representar as 
coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao 
qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na 
origem (x = y = 0).
'''
entrada = input()
x, y = entrada.split()

x = float(x)
y = float(y)

if x > 0 and y > 0:
    print("Q1")
elif x > 0 and y < 0:
    print("Q4")
elif x < 0 and y < 0:
    print("Q3")
elif x < 0 and y > 0:
    print("Q2")
elif x == 0 and y != 0:
    print("Eixo Y")
elif y == 0 and x != 0:
    print("Eixo X")
else:
    print("Origem")