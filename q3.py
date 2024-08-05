# 3) Faça um programa no qual o usuário precisa cadastrar as informações de dois produto: código, nome, quantidade e preço. 
# No final o programa deve mostrar as informações cadastradas e exibir o valor total das compras.


codigo1 = input("Digite o código do primeiro produto: ")
produto1 = input("Digite o nome do primeiro produto: ")
quantidade1 = int(input("Digite a quantidade do primeiro produto: "))
preço1 = float(input("Digite o preço do primeiro produto: R$ "))

codigo2 = input("Digite o código do segundo produto: ")
produto2 = input("Digite o nome do segundo produto: ")
quantidade2 = int(input("Digite a quantidade do segundo produto: "))
preço2 = float(input("Digite o preço do segundo produto: R$ "))

total1 = quantidade1 * preço1
total2 = quantidade2 * preço2

total = total1 + total2

# print(f"O código do prouto é: {codigo}. O nome do produto é: {produto}. Quantidade: {quantidade}. O valor unitário é R$ {preço}. O total é R$ {total}")

print("...........................................................")
print(f"Código          ---------- {codigo1}")
print(f"Produto         ---------- {produto1}")
print(f"Quantidade      ---------- {quantidade1}")
print(f"Valor Unitário  ---------- R$ {preço1:.2f}")
print("")
print(f"Código          ---------- {codigo2}")
print(f"Produto         ---------- {produto2}")
print(f"Quantidade      ---------- {quantidade2}")
print(f"Valor Unitário  ---------- R$ {preço2:.2f}")
print("")
print (f"Valor Total =  --------------------------- {total:.2f}")