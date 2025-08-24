'''
A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:
- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
'''

PI = 3.14159
entrada = float(input())
raio = entrada ** 2
saida = PI * raio
print(f"A={saida:.4f}")