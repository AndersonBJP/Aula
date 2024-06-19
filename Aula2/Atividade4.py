valor_da_compra = float(input("Digite o valor da compra: "))

valor = int(valor_da_compra)

if valor_da_compra >= 250:
    print("PARABÉNS! Você cumpriu com o requisito da promoção de 10 porcento! Mas falta pouco para a promoção de 30 porcento!")
elif valor_da_compra < 250:
    print("Poxa! Falta pouco para você conseguir a promoção de 10 porcento de desconto em sua compra!")
elif valor_da_compra >= 500:
    print("PARABÉNS! Você conseguiu um super desconto de 30 porcento!")
else:
    print("Poxa! Falta pouco para você conseguir a promoção de 30 porcento!")


