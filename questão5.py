import os

os.system("clear")

n1 = int(input("Digite um número: "))
operador = input("Digite a operação que deseja (+ - * /): ")

n2 = int(input("Digite um número: "))


match operador:
    case "+":
        resultado = n1 + n2

    case "-":
        resultado = n1 - n2

    case "*":
        resultado = n1 * n2

    case "/":
        resultado = n1 / n2
        
    case _:
        resultado = "Opção inválida"


print(f"Resultado: {resultado}")