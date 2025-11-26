from sympy import Symbol, sympify, integrate, diff, pi, E



x = Symbol('x')

def calcular_integral_indefinida():
    funcao_texto = input("Digite a função f(x): ")

    funcao = sympify(funcao_texto)
    integral_indef = integrate(funcao, x)

    print("\nResultado da integral indefinida")
    print(f"∫ {funcao_texto} dx = {integral_indef} + C\n")


def calcular_integral_definida():
    funcao_texto = input("Digite a função f(x): ")
    limite_inferior_texto = input("Digite o limite inferior: ")
    limite_superior_texto = input("Digite o limite superior: ")

    funcao = sympify(funcao_texto)
    limite_inferior = sympify(limite_inferior_texto)
    limite_superior = sympify(limite_superior_texto)

    resultado = integrate(funcao, (x, limite_inferior, limite_superior))

    print("\n Resultado da integral definida")
    print(f"∫[{limite_inferior}, {limite_superior}] {funcao_texto} dx = {resultado}\n")


def calcular_derivada():
    funcao_texto = input("Digite a função f(x): ")

    funcao = sympify(funcao_texto)
    derivada = diff(funcao, x)


    print("\n RESULTADO DA DERIVADA ")
    print(f"f'(x) = {derivada}\n")



while True:
    print("=== CALCULADORA DE CÁLCULO ===")
    print("1 - Derivada")
    print("2 - Integral Indefinida")
    print("3 - Integral Definida")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        calcular_derivada()

    elif opcao == "2":
        calcular_integral_indefinida()

    elif opcao == "3":
        calcular_integral_definida()

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida! Tente novamente.\n")
