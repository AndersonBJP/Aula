#Criando tupla
linguagens_tupla = ('Java', 'Python', 'Golang', 'C#', 'Javascript')

#Tupla transformada em lista
linguagens_lista = list(linguagens_tupla)
print("Tupla transformada em lista")

print(type(linguagens_lista))

#Adicionando 2 elementos com extend

linguagens_lista.extend(["Ruby", "Malbolge"])
print("Lista com 2 dados adicionados")
print(linguagens_lista)

linguagens_lista.pop(0)

print("Lista com Java removido")
print(linguagens_lista[0])

print("Primeiro elemento:")
print(linguagens_lista[0])

print("Quantidade de elementos:")
print(len(linguagens_lista))

dicionario = {
    "Nome": "Anderson"
    "Idade": 20
    "Profissão": "profissão"
}
