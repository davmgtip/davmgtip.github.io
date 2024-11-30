import matplotlib.pyplot as plt
from random import randint

size = 10

x = [randint(5,15) for a in range(size)]
y = [a for a in range(size)]

plt.plot(x, y, marker="<")

plt.show()
