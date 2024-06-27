palavra = input("Digite uma palavra: ")
vogais = ('a, e, i, o, u')
contador_vogais = 0

for letra in palavra:
    if letra.lower() in vogais:
        contador_vogais += 1

print(f"A palavra '{palavra}' possui {contador_vogais} vogais")




