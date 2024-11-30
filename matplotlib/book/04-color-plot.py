import matplotlib.pyplot as plt
import random

x = [random.randint(1,10) for a in range(10)]
y = [a for a in range(10)]

plt.plot(x,y, color="#aaaaaa")
plt.show()