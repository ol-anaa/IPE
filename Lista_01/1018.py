valor = int(input())
resto = valor  # inicializa o resto com o valor total

notas_cem = resto // 100
resto = resto % 100

notas_cinquenta = resto // 50
resto = resto % 50

notas_vinte = resto // 20
resto = resto % 20

notas_dez = resto // 10
resto = resto % 10

notas_cinco = resto // 5
resto = resto % 5

notas_dois = resto // 2
resto = resto % 2

notas_um = resto

print(valor)
print(f"{notas_cem} nota(s) de R$ 100,00")
print(f"{notas_cinquenta} nota(s) de R$ 50,00")
print(f"{notas_vinte} nota(s) de R$ 20,00")
print(f"{notas_dez} nota(s) de R$ 10,00")
print(f"{notas_cinco} nota(s) de R$ 5,00")
print(f"{notas_dois} nota(s) de R$ 2,00")
print(f"{notas_um} nota(s) de R$ 1,00")
