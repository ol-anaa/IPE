'''
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida 
(em Km) e o total de combustível gasto (em litros).
'''
# Distancia KM 
# Combustivel L

dist = int(input())
comb = float(input())

print(f"{dist/comb:.3f} km/l")