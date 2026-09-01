import numpy as np

print(format(0.1, '.20f'))

x = 0.1 + 0.1 + 0.1
y = 0.3

# ej 1
print(x == y)

print(format(x, '.20f'), format(y, '.20f'))

a = 1.0
#while a != 0.1:
while a > 0.1:
    print(a)
    a = a - 0.1 # el problema esta en esta resta de aca, se podria arreglar cambiando el != por un mayor
print('fin')