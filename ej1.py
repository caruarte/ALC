import numpy as np

A = np.array([[1j, -1-1j, 0], [1,-2,1],[1,2j,-1]])

B = np.array([-1,0,2j])

print(np.linalg.solve(A, B)) # solo sirve si hay solucion unica