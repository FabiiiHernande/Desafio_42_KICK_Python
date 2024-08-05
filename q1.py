# 1) Faça um programa em que o usuário digita dois valores e o resultado da soma é exibido na tela

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

print("................................................................")
print(f"O número {n1} mais o número {n2} é igual a {soma}")
print("................................................................")
print(f"O número {n1} menos o número {n2} é igual a {subtracao}")
print("................................................................")
print(f"O número {n1} vezes o número {n2} é igual a {multiplicacao}")
print("................................................................")
print(f"O número {n1} dividido pelo número {n2} é igual a {divisao}")
print("................................................................")