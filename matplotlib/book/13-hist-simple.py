import matplotlib.pyplot as plt
import random

x = [random.randint(1,50) for a in range(50)]

plt.hist(x=x, bins=3, cumulative=True)
plt.show()