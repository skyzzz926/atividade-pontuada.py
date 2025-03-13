import os

os.system("clear")

qtd_morango=int(input("Digite a quantidade de morangos(kg): " ))

qtd_macas=int(input("Digite a quantidade de macas(kg): " ))

if qtd_morango <= 5:
    valor_mor = qtd_morango * 2.50

if qtd_morango > 5:
    valor_mor = qtd_morango * 2.20

if qtd_macas <= 5:
    valor_mac = qtd_macas * 1.80

if qtd_macas > 5:
    valor_mac = qtd_macas * 1.50

totalfrutas = qtd_macas + qtd_morango
valortotal = valor_mac + valor_mor

if totalfrutas > 10 or valortotal > 15:
    valor = (valortotal * 0.9)
    print(f"Ganhou desconto de 10%, valor final: {valor}")
    
else:
    print(f"Valor final: {valortotal}")