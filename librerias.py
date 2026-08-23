import numpy as np

def esCuadrada(A):
    return A.ndim == 2 and A.shape[0] == A.shape[1]

def triangSup(A):
    B = A.copy()
    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            if j <= i:
                B[i][j] = 0
    return B

def triangInf(A):
    B = A.copy()
    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            if j >= i:
                B[i][j] = 0
    return B

def diagonal(A):
    B = A.copy()
    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            if j != i:
                B[i][j] = 0
    return B

def traza(A):
    res = 0
    for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                if i==j:
                    res += A[i][j]
    return res

def traspuesta(A):
    B = np.zeros(A.shape)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            B[i][j] = A[j][i]
    return B

def esSimetrica(A):
    if A.shape[0] != A.shape[1]:
        return False
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if A[i][j] != A[j][i]:
                return False
    return True

def calcularAx(A,x):
    B = np.zeros(A.shape[0])
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            B[i] += A[i][j] * x[j]
    return B

def intercambiarFilas(A,i,j):
    B = A[j].copy()
    A[j] = A[i]
    A[i] = B

def sumar_fila_multiplo(A, i, j, s):
    A[i] = A[i]+A[j]*s

def esDiagonalmenteDominante(A):
    for i in range(A.shape[0]):
        fila = 0
        for j in range(A.shape[1]):
            if i!=j:
                fila += abs(A[i][j])
        if abs(A[i][i]) <= fila:
            return False
    return True

def matrizCirculante(v):
    A = np.zeros((v.shape[0], v.shape[0]))
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            A[i][j] = v[j-i]
    return A

def matrizVandermonde(v):
    A = np.zeros((v.shape[0], v.shape[0]))
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            A[i][j] = v[j]**(i)
    return A    

def fibonacci(n):
    if n<=1:
        return n
    return np.linalg.matrix_power(np.array([[1,1],[1,0]]),n)[0][1]

def numeroAureo(n):
    return fibonacci(n+1) / fibonacci(n)

def matrizFibonacci(n):
    A=np.zeros((n,n))
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            A[i][j] = fibonacci(i) + fibonacci(j)
    return A

def matrizHilbert(n):
    A=np.zeros((n,n))
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            A[i][j] = 1 / (i+j+1)
    return A  

def pol1(x):
    return x**5 - x**4 + x**3 - x**2 + x - 1


def pol2(x):
    return x**2 + 3


def pol3(x):
    return x**10 - 2

def calcular100Puntos():
    x = np.linspace(-1, 1, 100)

    V = traspuesta(matrizVandermonde(x))

    c1 = [-1, 1, -1, 1, -1, 1]
    c2 = [3, 0, 1]
    c3 = [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

    p1 = calcularAx(V[:, :6], c1)
    p2 = calcularAx(V[:, :3], c2)
    p3 = calcularAx(V[:, :11], c3)

    print(p1)
    print(p2)
    print(p3)


def row_echelon(M):
    """ 
        Retorna la Matriz Escalonada por Filas 
    """
    A = np.copy(M)
    if (issubclass(A.dtype.type, np.integer)):
        A = A.astype(float)
    # Si A no tiene filas o columnas, ya esta escalonada
    f, c = A.shape
    if f == 0 or c == 0:
        return A
    # buscamos primer elemento no nulo de la primera columna
    i = 0
    while i < f and A[i,0] == 0:
        i += 1
    if i == f:
        # si todos los elementos de la primera columna son ceros
        # escalonamos filas desde la segunda columna
        B = row_echelon(A[:,1:])
        # y volvemos a agregar la primera columna de zeros
        return np.block([A[:,:1], B])
    # intercambiamos filas i <-> 0, pues el primer cero aparece en la fila i
    if i > 0:
        i = np.argmax(abs(A),0)[0]
        A[[0,i],:] = A[[i,0],:]
    # PASO DE TRIANGULACION GAUSSIANA:
    # a las filas subsiguientes les restamos un multiplo de la primera
    A[1:,:] -= (A[0,:] / A[0,0]) * A[1:,0:1]
    # escalonamos desde la segunda fila y segunda columna en adelante
    B = row_echelon(A[1:,1:])
    # reconstruimos la matriz por bloques adosando a B la primera fila 
    # y la primera columna (de ceros)
    return np.block([ [A[:1,:]], [ A[1:,:1], B] ])

A = np.array([[ 0,  1,  2,  3],
                [ 4,  5,  6,  7],
                [ 8,  9, 10, 11],
                [12, 13, 14, 15]])
B = np.array([[ 0,  1,  2,  3],
                    [ 4,  5,  6,  7],
                    [ -8,  9, 10, 11]])

C = np.array([[ 0,  1,  2,  3],
            [ 1,  5,  6,  7],
            [ 2,  6, 10, 11],
            [3, 7, 11, 15]])

D = np.array([[ 0,  1,  2,  3],
            [ 1,  5,  6,  7],
            [ 2,  6, 10, 11]])

E = np.array([[ -5,  1,  2],
            [ 1,  6,  4],
            [ 2,  0, -3]])

x = np.array([1,2,3,4])

print(A)
assert(esCuadrada(A))
assert not (esCuadrada(B))

print(triangSup(A))
print(triangInf(A))
print(diagonal(A))
print(traza(A))
print(traspuesta(A))
print(esSimetrica(A))
print(esSimetrica(C))
print(esSimetrica(D))
print(calcularAx(A,x))
intercambiarFilas(A, 1,2)
print(A)
sumar_fila_multiplo(A,0,2,3)
print(A)
print(esDiagonalmenteDominante(E))
print(matrizCirculante(np.array([1,2,3])))
print(matrizVandermonde(np.array([1,2,3,4])))
print(numeroAureo(10))
print(matrizFibonacci(5))
print(matrizHilbert(5))
print(np.linspace(0,10,5))
print(row_echelon(B))
calcular100Puntos()
print(fibonacci(5))