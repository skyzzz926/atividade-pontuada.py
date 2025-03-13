import os

os.system("clear")

combustivel = str(input("Digite o tipo de combustivel (A - Alcool/ G - Gasolina): " ))

litros = int(input("Digite o número de litros: "))

match combustivel:
    case 'A':
        if litros <= 25:
            valor = (3.79 * 0.98)* litros
            print(f"O desconto é de 2%, total a pagar é: {valor:.2f}")

        if litros > 25:
            valor = (3.79 * 0.96)* litros
            print(f"O desconto é de 4%, total a pagar é: {valor:.2f}")

    case 'G':
        if litros <= 25:
            valor = (6.59 * 0.97)* litros
            print(f"O desconto é de 3%, total a pagar é: {valor:.2f}")
            
        if litros > 25:
            valor = (6.59 * 0.95)* litros
            print(f"O desconto é de 5%, total a pagar é: {valor:.2f}")

    
        
        