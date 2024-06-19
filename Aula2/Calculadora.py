lista_operadores = ['+', '-', '*', '/']

Operador = input("Digite um operador aritmético: ")
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

match Operador:
    case '+':
        print(n1 + n2)
    case '-':
        print(n1 - n2)
    case '*':
        print(n1 * n2)
    case '/':
        print(n1 / n2)
    case _:
        print("Essa operação não é válida!")