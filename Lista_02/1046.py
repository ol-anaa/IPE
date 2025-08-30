'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo 
pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
'''
entrada =  input()
inicio, final = entrada.split()

inicio = int(inicio)
final = int(final)
hrs = 0

if inicio > final:
    hrs = 24 - inicio
    hrs = hrs + final
elif inicio == final:
    hrs = 24
else:
    hrs = final - inicio
    
print(f"O JOGO DUROU {hrs} HORA(S)")