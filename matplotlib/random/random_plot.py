import matplotlib.pyplot as plt
import random

x = [random.randint(1,10**5) for x in range(100)]
y = [random.randint(1,10**5) for x in range(100)]

plt.plot(x, y)
plt.show()