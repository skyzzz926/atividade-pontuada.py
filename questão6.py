import os

os.system("clear")

n1 = int(input("Digite a primeira nota: "))

n2 = int(input("Digite a segunda nota: "))
média = float

média = (n1 + n2)/2

if média >= 6:
    print("Parabéns! Você foi aprovado.")

if média >= 4 and média < 6:
    print("Você está em recuperação.")
    
if média < 4:
    print("Você foi reprovado :(")