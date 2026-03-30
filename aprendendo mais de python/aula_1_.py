valor = float(input("Digite o valor da compra: "))
cliente = input("Cliente VIP? (s/n): ")

if cliente == "s":
    desconto = valor * 0.2
else:
    desconto = valor * 0.1

valor_final = valor - desconto

if valor_final >= 100:
    print("Frete grátis")
else:
    print("Frete pago")

print("Valor final:", valor_final)
