import math
def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b): 
    return a * b
def dividir(a, b):
    return a / b
def potenciação(a, b):
    return a**b
def radiciação(a):
    return math.sqrt(a)
while True:
    print(" ")
    print("===Bem-vindo a Calculadora Simples===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potênciação")
    print("6. Radiciação")
    print("7. Desligar")
    print(" ")

    try:
        opção = int(input("Escolha uma opção: "))
        print(" ")

        #SOMAR
        if opção == 1:
            print("---Soma---")
            print(" ")
            try:
                primeiro_numero = float(input("Primeira parcela: "))
                segundo_numero = float(input("Segunda parcela: "))
                resultado = somar(primeiro_numero, segundo_numero)
                print(f"Resultado (Soma/Total): {resultado}")
            except ValueError:
                print("Expressão inválida")

        #SUBTRAIR
        elif opção == 2:
            print("---Subtração---")
            print(" ")
            try:
                primeiro_numero = float(input("Minuendo: "))
                segundo_numero = float(input("Subtraendo: "))
                resultado = subtrair(primeiro_numero, segundo_numero)
                print(f"Resultado (Resto/Diferença): {resultado}")
            except ValueError:
                print("Expressão inválida")


        #MULTIPLICAR
        elif opção == 3:
            print("---Multiplicação---")
            print(" ")
            try:
                primeiro_numero = float(input("Primeiro fator: "))
                segundo_numero = float(input("Segundo fator "))
                resultado = multiplicar(primeiro_numero, segundo_numero)
                print(f"Resultado (Produto): {resultado}")
            except ValueError:
                print("Expressão inválida")

        #DIVIDIR
        elif opção == 4:
            print("---Divisão---")
            print(" ")
            try:
                primeiro_numero = float(input("Dividendo: "))
                segundo_numero = float(input("Divisor: "))
                if segundo_numero == 0:
                    print("Não é possível dividir por zero")
                else:
                    resultado = dividir(primeiro_numero, segundo_numero)
                    print(f"Resultado (Quociente): {resultado}")
            except ValueError:
                print("Expressão inválida")

        #POTENCIAÇÃO
        elif opção == 5:
            print("---Potenciação---")
            print(" ")
            try:
                primeiro_numero = float(input("Base: "))
                segundo_numero = float(input("Expoente: "))
                resultado = potenciação(primeiro_numero, segundo_numero)
                print(f"Resultado (Potência): {resultado}")
            except ValueError:
                print("Expressão inválida")

        #RAIZ
        elif opção == 6:
            print("---Radiciação---")
            print(" ")
            try:
                radicando = float(input("Radicando: "))
                if radicando < 0:
                    print("Não existe raiz quadrada para esse número")
                else:
                    resultado = radiciação(radicando)
                    print(f"Resultado (Raiz): {resultado}")
            
            except ValueError:
                print("Expressão inválida")

        #DESLIGAR
        elif opção == 7:
            print("Desligando...")
            break

        else:
            print("Opção inválida")
    except ValueError:
        print("Expressão inválida")