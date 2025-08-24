'''
Dois carros (X e Y) partem em uma mesma direção. O carro X sai com velocidade constante 
de 60 Km/h e o carro Y sai com velocidade constante de 90 Km/h.

Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilômetros do carro X,
ou seja, consegue se afastar um quilômetro a cada 2 minutos.

Leia a distância (em Km) e calcule quanto tempo leva (em minutos) para o carro Y tomar essa 
distância do outro carro.

X = 60 Km/h
Y = 90 Km/h

1h (60min) dps
Y = 30km + d --> 1km a cada 2 min (60 min / 2)
X = d 

Carro Y
60 min --> 30km
X      --> 1Km

30Km * X = 60min
60/30 = 2
2 min
'''
dist = int(input())

#Vx = 60
#Vy = 90
# Diferença X e Y é 30km/h
# 30Km/60min = 0.5Km/min

temp = dist / 0.5 

print(f"{temp:.0f} minutos")