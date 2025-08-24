'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, 
meses e dias
Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. 
Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 
363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.
'''

dias = int(input())

if dias < 365:
    meses = dias // 30
    dias = dias % 30
    print("0 ano(s)")
    print(f"{meses} mes(es)")
    print(f"{dias} dia(s)")
else:
    anos = dias // 365
    resto_dias = dias % 365

    if resto_dias > 30:
        meses = resto_dias // 30
        dias = resto_dias % 30
        print(f"{anos} ano(s)")
        print(f"{meses} mes(es)")
        print(f"{dias} dia(s)")
    else:
        print(f"{anos} ano(s)")
        print(f"0 mes(es)")
        print(f"{resto_dias} dia(s)")