import numpy as np

def norma(x, p): #ok
    """
    Devuelve la norma p del vector
    """
    if p == 'inf':
        return max(np.abs(x))
    
    s = 0.0
    for xi in x:
        s += np.abs(xi)**p
    return s**(1.0/p)

def normaliza(X, p): #ok
    """
    Recibe X, una lista de vectores no vacios, y un escalar p. Devuelve
    una lista donde cada elemento corresponde a normalizar los
    elementos de X con la norma p.
    """
    Y = []
    for x in X:
        n = norma(x, p)
        y = []
        if n == 0:
            for xi in x:
                y.append(0.0)
        else:
            for xi in x:
                y.append(xi / n)
        Y.append(y)
    return Y

def normaMatMC(A,q,p,Np):

    # Cada fila es un vector random de longitud n
    X = np.random.rand(Np, A.shape[1])

    # Con axis = 1, la operacion se hace en cada fila.
    # keepdims hace que no se colapse y devuelva un vector, sino que cada valor queda en una columna
    if p == 'inf':
        # por cada fila, agarro el maximo de la fila
        normas_p = np.max(np.abs(X), axis=1, keepdims=True)
    else:
        # por cada fila, suma todos los valores elevandolos a la p
        # despues toma la raiz p de todos los elementos de la matriz
        normas_p = np.sum(np.abs(X) ** p, axis=1, keepdims=True) ** (1 / p)

    # divide cada vector random por su norma p para normalizar y que la norma sea igual a 1
    X = X / normas_p

    # Multiplico A por cada vector random normalizado. (m x n) @ (n x Np) = (m x Np)
    # cada columna termina siendo Ax
    AX = A @ X.T

    # Ahora uso axis = 0, para que tome la norma q de la columna, en la cual esta Ax
    if q == 'inf':
        normas = np.max(np.abs(AX), axis=0)
    else:
        normas = np.sum(np.abs(AX) ** q, axis=0) ** (1 / q)
    
    # normas tiene todos los ||Ax||q con ||x|| = 1, solo falta buscar el max
    # argmax te da el indice del mayor valor
    max_idx = np.argmax(normas)

    # devuelve la maxima norma, y con esa misma posicion, en X va a estar el vector random normalizado
    return normas[max_idx], X[max_idx]

def normaExacta(A, p=[1, 'inf']): #ok
    """
    Devuelve la norma 1 o infinito de una matriz A.
    """

    A = np.array(A, float)

    max_col = np.max(np.sum(np.abs(A), axis=0))
    max_fila = np.max(np.sum(np.abs(A), axis=1))

    if p == 1:
        return max_col
    elif p == 'inf':
        return max_fila
    elif p == [1, 'inf']:
        return [max_col, max_fila]
    else:
        return None

def condMC(A, p): #ok
    """
    Devuelve el número de condición de A usando la norma inducida p.
    """
    n, m = A.shape

    inversa_A = np.linalg.inv(A)

    norma_A, _ = normaMatMC(A, p, p, Np=2000)
    norma_inversa_A, _ = normaMatMC(inversa_A, p, p, Np=2000)

    return norma_A * norma_inversa_A

def condExacto(A, p): #ok
    """
    Que devuelve el numero de condicion de A a partir de 
    la formula de la ecuacion (1) usando la norma p .
    """
    n, m = A.shape

    inversa_A = np.linalg.inv(A)

    if p == 1:
        norma_A = normaExacta(A)[0]
        norma_inversa_A = normaExacta(inversa_A)[0]

    elif p == 'inf':
        norma_A = normaExacta(A)[1]
        norma_inversa_A = normaExacta(inversa_A)[1]

    return norma_A * norma_inversa_A