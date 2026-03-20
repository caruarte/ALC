import numpy as np
import row_echelon

1 + 3
a = 7
b = a + 1
print("b = ", b)

#Vectores

v = np.array([1,2,3,-1])
w = np.array([2,3,0,5])
print("v + w = ", v + w)
print("2*v = ", 2*v)
print("v**2 = ", v**2)

# Matrices

A = np.array([[1,2,3,4,5], [0,1,2,3,4], [2,3,4,5,6], [0,0,1,2,3], [0,0,0,0,1]])
print(A)
print(A[0:2, 3:5]) # no se incluye la ultima
print(A[:2, 3:])
print(A[[0,2,4], :]) # las filas 0, 2 y 4
ind = np.array([0,2,4])
print(A[ind, ind]) # la posicion 0 de la fila 0, la posicion 2 de la fila 2 y a 4 de la fila 4
print(A[ind, ind[:, None]]) # la columnas 0, 2, y 4

#Numeros complejos
print(1j*1j) # j es i
print((1+2j)*1j)