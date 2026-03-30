def valor_compra():
    while True:
        try:
            valores = float(input("Digite o valor da compra: R$ "))
            if valores > 0:
                print("O valor para a compra foi registrado!")
            else:
                print("O valor para a compra NÃO pode ser ZERO ou NEGATIVO!")
            return
        except ValueError:
            print("Digite o valor certo!")
