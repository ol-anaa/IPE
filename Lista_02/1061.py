'''
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e 
terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que
ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração
deste evento.
'''

dia_inicial = int(input().split()[1])
h_inicial, m_inicial, s_inicial = map(int, input().split(" : "))

dia_final = int(input().split()[1])
h_final, m_final, s_final = map(int, input().split(" : "))

inicio = dia_inicial*86400 + h_inicial*3600 + m_inicial*60 + s_inicial
fim = dia_final*86400 + h_final*3600 + m_final*60 + s_final

duracao = fim - inicio

dias = duracao // 86400
duracao %= 86400
horas = duracao // 3600
duracao %= 3600
minutos = duracao // 60
segundos = duracao % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")