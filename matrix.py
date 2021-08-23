# Função auxiliar para imprimir a matriz de forma mais legível
def printM(m):
    print("[", end='')
    for i in range(len(m)):
        print(m[i], end=',')
        if i < len(m) - 1:
            print()
    print("]")

def lerMatrizUsandoInput(input):
    matriz = []
    linhas = input.split('\n')
    for linha in linhas:
        linhaFormatada = linha.split(' ')
        for i in range(len(linhaFormatada)):
            linhaFormatada[i] = int(linhaFormatada[i])
        matriz.append(linhaFormatada)
    return matriz

# Função auxiliar para geração de uma lista de zeros de tamamho N
def newLine(n):
    line = []
    for i in range(n):
        line.append(0)
    return line


# Determinante de matriz triangular
def detTriang(m):
    d = 1
    for i in range(len(m)):
        d = d * m[i][i]
    return d


# Retrosubstituição
def back(A, b):
    n = len(A)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        sigma = 0
        for j in range(i, n):
            sigma += A[i][j] * x[j]
        x[i] = (b[i] - sigma) / A[i][i]
    return x


# Substituição
def forw(A, b):
    n = len(A)
    x = [0] * n
    for i in range(n):
        sigma = 0
        for j in range(i, -1, -1):
            sigma += A[i][j] * x[j]
        x[i] = (b[i] - sigma) / A[i][i]
    return x


# Função para multiplicar duas matrizes
def multiplyM(a, b):
    n = len(a[0])
    rows = len(a)
    cols = len(b[0])
    c = []
    for i in range(rows):
        c.append(newLine(cols))
        for j in range(cols):
            for k in range(n):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
    return c


# Transpõe matriz
def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


# Calcula inversa de A (seja A=LU)
def invLU(L, U):
    id = []
    for i in range(len(L)):
        id.append([0] * len(L))
        id[i][i] = 1

    inv = []
    for row in id:
        y = forw(L, row)
        x = back(U, y)
        inv.append(x)

    inv = transpose(inv)
    return inv
