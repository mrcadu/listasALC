import choleskyDecomposition
import gaussSeidelDecomposition
import jacobiDecomposition
import luDecomposition
from matrix import *


def escreverOutput(output):
    file = open("output", "w")
    file.write(output)
    file.close()


def decompose():
    ordem = int(input("Digite a ordem do sistema de equações:\n"))
    icod = int(input("Digite o ICOD relativo ao método de análise\n"))
    idet = int(input("Determine se deverá ser realizado o cálculo do determinante.0 não calcula determinante/ maior "
                     "que 0 calcula o determinante\n"))
    matrizA = ""
    linhaMatriz = input(
        "Digite o valor da matriz A, cada elemento da linha será dividido por espaço e cada coluna será "
        "dividida com quebra de linha, após o término da digitação basta pressionar enter sem nada "
        "escrito\n")
    while linhaMatriz != "":
        matrizA += linhaMatriz
        linhaMatriz = input("")
        if linhaMatriz != "":
            matrizA += "\n"
    vetorB = input("Digite o valor do vetor b, cada elemento do vetor será dividido por espaço\n")
    vetorB = vetorB.split(" ")
    for i in range(len(vetorB)):
        vetorB[i] = int(vetorB[i])
    tolm = int(input("Digite a tolerância máxima para a solução iterativa\n"))
    matriz = lerMatrizUsandoInput(matrizA)

    if icod == 1:
        L, U, P, b = luDecomposition.decompose(matriz, vetorB)
        y = forw(L, b)
        x = back(U, y)
        print("Solução do Sistema = " + str(x))
        detA = detTriang(L) * detTriang(U) * P
        if idet != 0:
            print("O determinante da matriz é:" + detA)
    elif icod == 2:
        L, Lt = choleskyDecomposition.decompose(matriz, ordem)
        y = forw(L, vetorB)
        x = back(Lt, y)
        print("Solução do Sistema = " + str(x))
        return
    elif icod == 3:
        jacobiDecomposition.decompose()
        return
    elif icod == 4:
        gaussSeidelDecomposition.decompose()
        return


decompose()
