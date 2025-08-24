'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma 
fábrica, e informe-o expresso no formato horas:minutos:segundos.
'''
segundos = int(input())

if segundos < 60:
    print(f"0:0:{segundos}")
    
elif segundos > 60 and segundos <= 3600:
    minu = segundos // 60
    segundos = segundos % 60
    print(f"0:{minu}:{segundos}")
    
else:
    hrs = segundos // 3600
    resto = segundos % 3600
    
    if resto > 60:
        minu = resto // 60
        resto = resto % 60
        print(f"{hrs}:{minu}:{resto}")
    else:
        print(f"{hrs}:0:{resto}")