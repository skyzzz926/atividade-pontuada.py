import os

os.system("clear")

renda=float(input("Digite a renda mensal: " ))

emprestimo=float(input("Digite o valor total do empréstimo solicitado: " ))

prestacoes=int(input("Digite o número de prestações que o solicitante deseja pagar : " ))
qtd_prestacoes=emprestimo/prestacoes

if emprestimo <= (10*renda) and qtd_prestacoes <= (0.30*renda):
    print("Empréstimo Concedido!")
    
else:
    print("Empréstimo Negado!")