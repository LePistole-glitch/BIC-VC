import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return x
def func2(x):
    return x**2
def func3(x):
    return x**3

x = np.arange(0., 6., 0.2)

plt.plot(x, [func(i) for i in x], ls=":")
plt.plot(x, [func2(i) for i in x], ls=":")
plt.plot(x, [func3(i) for i in x], ls=":")
plt.show()