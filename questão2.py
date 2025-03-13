import os
os.system("clear")

nome = str(input("Digite o nome: " ))

sexo = str(input("Digite o sexo: " ))

estado_civil = str(input("Digite o estado civil da pessoa: " ))



print(f"O nome da pessoa é: {nome}")

print(f"O sexo da pessoa é: {sexo}")

print(f"O estado civil da pessoa é: {estado_civil}")

if sexo == 'F' and estado_civil == 'CASADA':
    
    anos = int(input("Digite o tempo de casada: " ))
    print(f"O tempo de casada da pessoa é: {anos}")