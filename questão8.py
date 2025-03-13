import os

os.system("clear")


opcao = str(input( """
\t Cor   \t Preço
                  
    Verde \t R$10,00
    Azul \t R$20,00
    Amarelo \t R$30,00
    Vermelho \t R$40,00


Digite a opção desejada:
"""))


match opcao:
    case 'Verde':
        print("Verde - R$10,00")

    case 'Azul':
        print("Azul - R$20,00")

    case 'Amarelo':
        print("Amarelo - R$30,00")
        
    case 'Vermelho':
        print("Vermelho - R$40,00")