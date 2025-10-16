'''
Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.
'''

list = []

for i in range(20):
    entrada = int(input())
    list.append(entrada)

for i in range(0, (len(list)// 2)):
    aux = list[i]
    list.pop(i)

    list.insert(i, list[len(list) - 1 - i])
    list.insert(len(list) - 1 - i, aux)

    list.pop(len(list) - 1 - i)
    

for index, num in enumerate(list):
    print(f"N[{index}] = {num}")

''' Ou simplesmente faça um list.reverse() que terá o mesmo resultado'''