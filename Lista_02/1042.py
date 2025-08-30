'''
Leia 3 valores inteiros e ordene-os em ordem crescente. 
No final, mostre os valores em ordem crescente, uma linha em
branco e em seguida, os valores na sequência como foram lidos.
'''
entrada = input()
nums = list(map(int, entrada.split()))

for n in sorted(nums):
    print(n)

print()

for n in nums:
    print(n)