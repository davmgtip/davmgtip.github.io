import time
import matplotlib.pyplot as plt
import random

try:
    while True:
        random.seed(time.time())
        x = [random.randint(1,5) for x in range(5)]
        plt.pie(x)
        plt.show()
except KeyboardInterrupt:
    exit(0)