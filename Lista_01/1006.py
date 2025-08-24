'''
Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. 
A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3
e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa 
decimal.
'''

A = float(input())
B = float(input())
C = float(input())

NOTA1 = A * 2
NOTA2 = B * 3
NOTA3 = C * 5

RESULT = (NOTA1 + NOTA2 + NOTA3)/10

print(f"MEDIA = {RESULT:.1f}")