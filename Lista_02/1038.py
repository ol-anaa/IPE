'''
Com base na tabela abaixo, escreva um programa que leia o código de um 
item e a quantidade deste item.
A seguir, calcule e mostre o valor da conta a pagar.
'''

entrada = input()
cod, qtd = entrada.split()

cod = int(cod)
qtd = int(qtd)

def result(cod, qtd):
    match cod:
        case 1:
            return qtd * 4
        case 2:
            return qtd * 4.50
        case 3:
            return qtd * 5
        case 4:
            return qtd * 2
        case 5:
            return qtd * 1.50
        case _:
            return "Error!!"

print(f"Total: R$ {result(cod, qtd):.2f}")
