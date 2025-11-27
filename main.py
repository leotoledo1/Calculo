from sympy import Symbol, sympify, integrate, diff
import numpy as np
import matplotlib.pyplot as plt

x = Symbol('x')

def calcular_integral_indefinida():
    funcao_texto = input("Digite a função f(x): ")

    funcao = sympify(funcao_texto)
    integral_indef = integrate(funcao, x)

    print("\nResultado da integral indefinida")
    print(f"∫ {funcao_texto} dx = {integral_indef} + C\n")


def calcular_integral_definida():
    funcao_texto = input("Digite a função f(x): ")
    limite_inferior_texto = input("Digite o intervalo inferior: ")
    limite_superior_texto = input("Digite o intervalo superior: ")

    funcao = sympify(funcao_texto)
    a = sympify(limite_inferior_texto)
    b = sympify(limite_superior_texto)

    resultado = integrate(funcao, (x, a, b))

    print("\nResultado da integral definida")
    print(f"∫[{a}, {b}] {funcao_texto} dx = {resultado}\n")

    try:
        f = lambda val: float(funcao.subs(x, val))

        a_f = float(a)
        b_f = float(b)

        xs = np.linspace(a_f - (b_f - a_f) * 0.3, b_f + (b_f - a_f) * 0.3, 500)
        ys = [f(val) for val in xs]

        plt.plot(xs, ys, label=f"f(x) = {funcao_texto}", linewidth=2)

        plt.title(f"Gráfico de f(x) = {funcao_texto}\nIntegral = {float(resultado):.5f}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()

    
        plt.axvline(a_f, linestyle="--", color="black")
        plt.axvline(b_f, linestyle="--", color="black")

        plt.show()

    except Exception as e:
        print(f"Erro ao gerar o gráfico: {e}")


def calcular_derivada():
    funcao_texto = input("Digite a função f(x): ")

    funcao = sympify(funcao_texto)
    derivada = diff(funcao, x)

    print("\nRESULTADO DA DERIVADA")
    print(f"f'(x) = {derivada}\n")


while True:
    print("CALCULADORA")
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
