import matplotlib.pyplot as plt

x = [a for a in range(100)]
y = [a for a in range(50)] + [a for a in range(50, 0, -1)]
plt.bar(x,y)

plt.show()