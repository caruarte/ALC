import numpy as np

def rota(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])

def escala(s):
    M = np.eye(len(s))
    for i in range(len(s)):
        M[i][i] = M[i][i] * s[i]
    return M

def rota_y_escala(theta,s):
    rotar = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
    escalar = np.eye(2)
    for i in range(2):
        escalar[i][i] = escalar[i][i] * s[i]

    res = escalar@rotar

    return res

def afin(theta,s,b): # s y b son arrays de dos elementos, devuelve una matriz 3x3
    rotar = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
    escalar = np.eye(2)
    for i in range(2):
        escalar[i][i] = escalar[i][i] * s[i]

    escalarYrotar = escalar@rotar 

    res = np.zeros([3,3])
    for i in range(escalarYrotar.shape[0]):
        for j in range(escalarYrotar.shape[1]):
            res[i][j] = escalarYrotar[i][j]
    res[2][2] = 1
    for i in range(len(b)):
        res[i][2] = b[i]
        
    return res

def trans_afin(v, theta,s,b):

    res = np.ones((3,1))
    for i in range(2):
        res[i][0] = v[i]
    res = afin(theta, s, b)@res
    resultado = np.zeros((2,1))
    for i in range(2):
        resultado[i] = res[i]
    resultado = resultado.reshape((2,))
    return resultado

   