import matplotlib.pyplot as plt
import numpy as np

vals = np.arange(0,10,0.1)

a = np.sin(vals)
b = np.cos(vals)
c = np.tan(vals)

plt.plot(vals,a)
plt.plot(vals,b)
plt.plot(vals,c)

plt.show()