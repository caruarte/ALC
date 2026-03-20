import numpy as np
import row_echelon

# v1 = np.array([10, 5, -7, 1])
# print(v1)

# v2 = np.array([5, 0, 3/2, 2])
# print(v2)

# A = np.array([[1,2],[3,4]]) # Matriz de 2 x 2
# print("A = \n", A)
# B = np.array([[1,2,3,4],[7,1,2,-1]]) # Matriz de 4 x 2
# print("B = \n", B)
# C = np.array([[1], [7], [1/3]]) # Matriz columna de 1 x 3
# print("C = \n", C)


# v1 = np.array([1,2,5,10])
# print("v1[2] = ", v1[2])
# A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print("A[2,3] = ", A[2,3])

# v1 = np.array([10, 5, -7, 1])
# v2 = np.array([5, 0, 7, 2])
# print("v1 + v2 = ", v1 + v2)

# A1 = np.array([[1,2],[3,4]])
# print("A1 = \n", A1)
# A2 = np.array([[2,7],[1,0]])
# print("A2 = \n", A2)
# A3 = np.array([[2,7,1,0]])
# print("A3 = \n", A3)
# print("A1 + A2 = \n", A1 + A2) # Matriz de 2 x 2
# # No podemos sumar matrices de distinto tamaño

# # DIAGONALIZAR
# A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(row_echelon.row_echelon(A))

#ARMAR MATRIZ AMPLIADA

A = np.array([[1,5,5],[2,2,-3],[-1,-9,2]])
b = np.array([2, -1, 9])
Ab = np.c_[A, b] # Las matrices o vectores van entre corchetes.
print("Ab = \n", Ab)
print("Matriz escalonada: \n", row_echelon.row_echelon(Ab))

