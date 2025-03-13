import os

os.system("clear")

nome=str(input("Digite o nome do produto: " ))

qtd=int(input("Digite a quantidade: " ))

preco=float(input("Digite o preço: " ))

total = float

total = qtd * preco


if qtd <= 5:
    pagar  = total - (2/100)
    print(f"O desconto é de 2%, total a pagar é: {pagar}")

if qtd > 5 and qtd <= 10:
    pagar = total - (3/100)
    print(f"O desconto é de 3%, total a pagar é: {pagar}")
    
if qtd > 10:
    pagar = total - (5/100)
    print(f"O desconto é de 5%, total a pagar é: {pagar}")