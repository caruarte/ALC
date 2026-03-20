import numpy as np
import matplotlib.pyplot as plt

xx = np.array([1,2,3])
yy = np.array([1,2,0])
x = np.linspace(0,4,100)

f = lambda t: a*t**2+b*t+c

plt.plot(xx, yy, '*')
plt.plot(x,f(x))
plt.show()

a^2+b+c = 1
4a + 2b+c = 2
9a + 3b + c = 0
