idade_str = input("Digite sua idade: ")

idade = int(idade_str)

if idade > 18:
    print("Indivíduo possui idade mínima para dirigir.")
elif idade >= 17:
    print("Indivíduo tem entre 17 e 18 anos e NÃO está apto para dirigir.")
else:
    print("Indivíduo não possui idade mínima para dirigir.")