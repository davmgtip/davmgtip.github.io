# Question:
# Given array: [1, 2, 21, 35, 35, 21, 7, 1]
# To plot: sin, cos and tan for all three values


import matplotlib.pyplot as plt
import numpy as np

data = [1, 2, 21, 35, 35, 21, 7, 1]

plt.plot([a for a in range(len(data))], np.sin(data), color="cyan")
# plt.plot(data, np.cos(data))
# plt.plot(data, np.tan(data))

plt.show()