'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do 
jogo.
Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
'''
entrada = input().split()
HI, MI, HF, MF = map(int, entrada)

inicio = HI * 60 + MI
fim = HF * 60 + MF

if fim <= inicio:
    fim += 24 * 60

duracao = fim - inicio
hrs = duracao // 60
min = duracao % 60

print(f"O JOGO DUROU {hrs} HORA(S) E {min} MINUTO(S)")