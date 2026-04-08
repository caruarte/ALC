import numpy as np
import matplotlib.pyplot as plt

xx = np.array([1,2,3])
yy = np.array([1,2,0])
x = np.linspace(0,4,100)

f = lambda t: (-3/2)*t**2+(11/2)*t+(-3)

plt.plot(xx, yy, '*')
plt.plot(x,f(x))
plt.show()


