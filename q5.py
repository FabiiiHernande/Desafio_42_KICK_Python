# 5) Faça um programa que calcule a área de um quadrado/retângulo.

lado = float(input("Digite o valor do lado do quadrado: "))
areaq = lado * 2
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
arear = base * altura

print("")
print(f"A área do quadrado é {areaq:.2f}")
print("")
print(f"A área do retângulo é {arear:.2f}")
print("")