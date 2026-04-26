#Aqui está a definição para cada operação matemática desejada.
import time
while True:
    print("Qual operação você deseja realizar?")
    print("S = Soma")
    print("SB = Subtração")
    print("M = Multiplicação")
    print("D = Divisão")
    print("R = Raiz Quadrada")
    print("SAIR = Encerrar o programa")

    operacao = input("Digite a operação correspondente: ")

    if operacao == 'SAIR':  
        print("Encerrando Programa...\n")
        time.sleep(1)
        print("Programa encerrado.\n")
        break

    if operacao == 'S':
        print("Você escolheu Soma")
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))

    elif operacao == 'SB':
        print("Você escolheu Subtração")
        num1 = float(input("DIgite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))

    elif operacao == 'M':
        print("Você escolheu Multiplicação")
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))

    elif operacao == 'D':
        print("Você escolheu Divisão")
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))

    elif operacao == 'R':
        print("Você escolheu Raiz Quadrada")
        num1 = float(input("Digite o primeiro número:"))

    else:
        print("\n\033[31m Operação inválida pelo sistema. Escolha uma operação válida.\n\033[0m")
        continue

    if operacao == 'S':
        resultado = num1 + num2
    elif operacao == 'SB':
        resultado = num1 - num2
    elif operacao == 'M':
        resultado = num1 * num2
    elif operacao == 'D':
        if num2 == 0:
            resultado = "Divisão por zero não é permitda"
        else:
            resultado = num1 / num2
    elif operacao == 'R':
        if num1 < 0:
            resultado = "Raiz quadrada de número negativo não é permitida"
        else:
            resultado = num1 ** 0.5

    if operacao in ['S', 'SB', 'M', 'D', 'R']:
        print(f"O resultado da operação {operacao} é: {resultado}")
    print("\n")  # Adiciona uma linha em branco para melhor legibilidade
    
    time.sleep(2.5)  # Pausa de 2.5 segundos para melhor visualização

    print("Continuando o programa...\n")  # Mensagem de continuação do programa