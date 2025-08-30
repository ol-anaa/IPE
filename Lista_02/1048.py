'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário	Percentual de Reajuste
0 - 400.00
400.01 - 800.00
800.01 - 1200.00
1200.01 - 2000.00
Acima de 2000.00

15%
12%
10%
7%
4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice
reajustado, em percentual.
'''
sal = float(input())
newSal = 0
reajuste = 0
percent = 0

if sal <= 400:
    percent = 15
    reajuste = sal * (percent/100)
    newSal = reajuste + sal

elif sal > 400 and sal <= 800:
    percent = 12
    reajuste = sal * (percent/100)
    newSal = reajuste + sal

elif sal > 800 and sal <= 1200:
    percent = 10
    reajuste = sal * (percent/100)
    newSal = reajuste + sal
    
elif sal > 1200 and sal <= 2000:
    percent = 7
    reajuste = sal * (percent/100)
    newSal = reajuste + sal
    
else:
    percent = 4
    reajuste = sal * (percent/100)
    newSal = reajuste + sal
    
print(f"Novo salario: {newSal:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percent} %")