'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor 
monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode 
ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. 
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
A seguir mostre a relação de notas necessárias.
'''

valor = float(input())

centavos = int(round(valor * 100))

notas_100 = centavos // 10000
centavos %= 10000

notas_50 = centavos // 5000
centavos %= 5000

notas_20 = centavos // 2000
centavos %= 2000

notas_10 = centavos // 1000
centavos %= 1000

notas_5 = centavos // 500
centavos %= 500

notas_2 = centavos // 200
centavos %= 200

# moedas
moeda_1 = centavos // 100
centavos %= 100

moeda_050 = centavos // 50
centavos %= 50

moeda_025 = centavos // 25
centavos %= 25

moeda_010 = centavos // 10
centavos %= 10

moeda_005 = centavos // 5
centavos %= 5

moeda_001 = centavos

print("NOTAS:")
print(f"{notas_100} nota(s) de R$ 100.00")
print(f"{notas_50} nota(s) de R$ 50.00")
print(f"{notas_20} nota(s) de R$ 20.00")
print(f"{notas_10} nota(s) de R$ 10.00")
print(f"{notas_5} nota(s) de R$ 5.00")
print(f"{notas_2} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{moeda_1} moeda(s) de R$ 1.00")
print(f"{moeda_050} moeda(s) de R$ 0.50")
print(f"{moeda_025} moeda(s) de R$ 0.25")
print(f"{moeda_010} moeda(s) de R$ 0.10")
print(f"{moeda_005} moeda(s) de R$ 0.05")
print(f"{moeda_001} moeda(s) de R$ 0.01")
