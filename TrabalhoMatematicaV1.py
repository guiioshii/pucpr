import sys
import numpy as np
programa = True
from sympy import *
from sympy.plotting import *


def gerar_grafico2(a, b):

    x = Symbol('x')
    y = a * b**x
    plot(y, xlim=[0, 10], ylim=[-5, 5])


def gerar_grafico1(b, c):

    x = Symbol('x')
    y = x**2 - b * x + c
    plot(y, xlim=[0, 10], ylim=[-5, 5])


def voltar_menu():
    menu = int(input("Deseja voltar ao menu[1] ou continuar nesse cálculo[2]?"))
    while menu != 1 and menu != 2:
        print("Parece que você digitou algo errado, tente novamente.")
        menu = int(input("Deseja voltar ao menu[1] ou continuar nesse cálculo[2]?"))
        print()
        if menu == 1:
            continue
        elif menu == 2:
            break




def calcular_func_expo():
    x = int(input("Agora, digite o valor de 'x':"))

    y = a * b**x

    print("f(x) =", y)


def verificar_a():
    if a > 0:
        print("A função é crescente.")
    elif a < 0:
        print("A função é decrescente.")


def calcular_vertice():
    delta = b * b -4 * a * c
    
    xv = - b / 2 * a
    yv = - delta / 4 * a
    
    if a < 0:
        print("O ponto máximo é:", "(", xv, ",", yv, ")")
    else:
        print("O ponto mínimo é:", "(", xv, ",", yv, ")")
    


def calcular_raizes():
    import math
    import cmath

    delta = b * b -4 * a * c
    
    if delta > 0:
        r_delta = math.sqrt(delta)
        x = (- b + r_delta) / 2 * a
        print("x' =", x)
        x1 = (- b - r_delta) / 2 * a
        print("x'' =", x1)
        
    else:
        r_delta = cmath.sqrt(delta)
        x = (- b + r_delta) / 2 * a
        print("x' =", x)
        x1 = (- b - r_delta) / 2 * a
        print("x'' =", x1)


def calcular_funcao():
    x = int(input("Agora, digite o valor de 'x':"))
    
    y = a * (x*x) + b * x + c
    
    print("O resultado dessa função é:", y)    
    
def calcular_determinante():
    if a == 2 and b == 2:
        mult = matriz[0][0] * matriz[1][1]
        mult1 = matriz[0][1] * matriz[1][0]
        resultado_determinante = mult + mult1
        print ("Determinante =", resultado_determinante)
    elif a == 3 and b == 3:
        mult = matriz[0][0] * matriz[1][1] * matriz[2][2]
        mult1 = matriz[0][2] * matriz[1][1] * matriz[2][0]
        resultado_determinante = mult + mult1
        print ("Determinante =", resultado_determinante)
    else: 
        print("Matriz nao e quadrada")

def multiplicar_matrizes():
    c = int(input("Digite o Numero de Linhas:"))
    d = int(input("Digite o Numero de Colunas:"))

    matriz1 = [0] * c
    for linha in range (c):
        matriz1[linha] = [0] * d
        
    matriz2 = [0] * c
    for linha in range (c):
        matriz2[linha] = [0] * d

    for linha in range (c):
        for coluna in range (d):
            matriz1[linha][coluna] = int(input("Digite os Numeros da matriz:"))

            print (matriz1)
    if b != c:
        print("Multiplicacao nao e possivel")
    
    else:
        for linha in range (c):
            for coluna in range (d):
                matriz2[linha][coluna] = matriz[linha][coluna] * matriz1[linha][coluna]
        print("AxB =", matriz2)

def transpor_matriz():
    matriz_transposta = np.array(matriz).T
    print("Matriz transposta", matriz_transposta)

while programa == True:
    menu_secundario = True
    print("Bem vindo.")
    print()
    print("[1]. Calcular função de segundo grau")
    print("[2]. Calcular função exponencial")
    print("[3]. Calcular matrizes")
    print("[4]. Sair")
    escolha = int(input("Digite sua escolha de 1 a 4:"))
    while escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
        print("Parece que você digitou algo errado, tente novamente.")
        escolha = int(input("Digite sua escolha de 1 a 4:"))
    if escolha == 1:
        a = int(input("Digite o valor de 'a':"))
        b = int(input("Digite o valor de 'b':"))
        c = int(input("Digite o valor de 'c':"))
        while menu_secundario == True:
            print()
            print("[1]. Calcular raízes")
            print("[2]. Calcular função em x pedido")
            print("[3]. Calcular vértice")
            print("[4]. Gerar gráfico")
            escolha_func2grau = int(input("Digite sua escolha de 1 a 4:"))
            while escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
                print("Parece que você digitou algo errado, tente novamente.")
                escolha_func2grau = int(input("Digite sua escolha de 1 a 4:"))
            if escolha_func2grau == 1:
                calcular_raizes()
                sair = int(input("Deseja encerrar a calculadora? Digite 1 se sim, digite qualquer outra coisa para 'não':"))
                if sair == 1:
                    sys.exit('Encerrando a calculadora')
                else:
                    voltar_menu()


            elif escolha_func2grau == 2:
                calcular_funcao()
                sair = int(
                    input("Deseja encerrar a calculadora? Digite 1 se sim, digite qualquer outra coisa para 'não':"))
                if sair == 1:
                    sys.exit('Encerrando a calculadora')
                else:
                    voltar_menu()

            elif escolha_func2grau == 3:
                calcular_vertice()
                sair = int(
                    input("Deseja encerrar a calculadora? Digite 1 se sim, digite qualquer outra coisa para 'não':"))
                if sair == 1:
                    sys.exit('Encerrando a calculadora')
                else:
                    voltar_menu()

            else:
                gerar_grafico1(b, c)
                sair = int(
                    input("Deseja encerrar a calculadora? Digite 1 se sim, digite qualquer outra coisa para 'não':"))
                if sair == 1:
                    sys.exit('Encerrando a calculadora')
                else:
                    voltar_menu()

    if escolha == 2:
        a = int(input("Digite o valor de 'a':"))
        b = int(input("Digite o valor de 'b':"))
        while menu_secundario == True:
            print("[1]. Verificar se a função é crescente ou decrescente")
            print("[2]. Calcular função em x pedido")
            print("[3]. Gerar gráfico")
            escolha_funcexpo = int(input("Digite sua escolha de 1 a 3:"))
            while escolha != 1 and escolha != 2 and escolha != 3:
                print("Parece que você digitou algo errado, tente novamente.")
                escolha_func2grau = int(input("Digite sua escolha de 1 a 3:"))
            if escolha_funcexpo == 1:
                verificar_a()
                sair = int(
                    input("Deseja encerrar a calculadora? Digite 1 se sim, digite qualquer outra coisa para 'não':"))
                if sair == 1:
                    sys.exit('Encerrando a calculadora')
                else:
                    voltar_menu()

            elif escolha_funcexpo == 2:
                calcular_func_expo()
                sair = int(
                    input("Deseja encerrar a calculadora? Digite 1 se sim, digite qualquer outra coisa para 'não':"))
                if sair == 1:
                    sys.exit('Encerrando a calculadora')
                else:
                    voltar_menu()

            else:
                gerar_grafico2(a, b)
                sair = int(
                    input("Deseja encerrar a calculadora? Digite 1 se sim, digite qualquer outra coisa para 'não':"))
                if sair == 1:
                    sys.exit('Encerrando a calculadora')
                else:
                    voltar_menu()


    elif escolha == 3:
        a = int(input("Digite o Numero de Linhas"))
        b = int(input("Digite o Numero de Colunas"))

        matriz = [0] * a
        for linha in range (a):
            matriz[linha] = [0] * b

        for linha in range (a):
             for coluna in range (b):
                 matriz[linha][coluna] = int(input("Digite os Numeros"))

                 print (matriz)
        while menu_secundario == True:
            print("[1]. Calcular determinante da matriz")
            print("[2]. Multiplicar matrizes")
            print("[3]. Matriz transposta")
            escolha_matriz = int(input("Digite sua escolha de 1 a 3:"))
            while escolha_matriz != 1 and escolha_matriz != 2 and escolha_matriz != 3:
                print("Parece que você digitou algo errado, tente novamente.")
                escolha_matriz = int(input("Digite sua escolha de 1 a 3:"))
            if escolha_matriz == 1:
                calcular_determinante()
                sair = int(
                    input("Deseja encerrar a calculadora? Digite 1 se sim, digite qualquer outra coisa para 'não':"))
                if sair == 1:
                    sys.exit('Encerrando a calculadora')
                else:
                    voltar_menu()
            elif escolha_matriz == 2:
                multiplicar_matrizes()
                sair = int(
                    input("Deseja encerrar a calculadora? Digite 1 se sim, digite qualquer outra coisa para 'não':"))
                if sair == 1:
                    sys.exit('Encerrando a calculadora')
                else:
                    voltar_menu()
            else:
                transpor_matriz()
                sair = int(
                    input("Deseja encerrar a calculadora? Digite 1 se sim, digite qualquer outra coisa para 'não':"))
                if sair == 1:
                    sys.exit('Encerrando a calculadora')
                else:
                    voltar_menu()

    if escolha == 4:
        sys.exit('Encerrando a calculadora')