import matplotlib.pyplot as plt
import random

possible_linestyles = [':', "-.", "--", "-"]
# equal to dotted, dashdot, dashed, solid

x = [random.randint(1,10) for a in range(10)]
y = [a for a in range(10)]

plt.plot(x,y, linestyle=random.choice(possible_linestyles))
plt.show()