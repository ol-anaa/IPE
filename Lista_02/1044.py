'''
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem 
"Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são 
múltiplos entre si.
'''
entrada = input()
Num1, Num2 = entrada.split()
Num1 = int(Num1)
Num2 = int(Num2)
result = 0

if Num1 > Num2:
    result = Num1 % Num2
else:
    result = Num2 % Num1
    
if result != 0:
    print("Nao sao Multiplos")
else:
    print("Sao Multiplos")