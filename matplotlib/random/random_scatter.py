import matplotlib.pyplot as plt
from random import randint, choice

def random_color():
    color_strings = "abcdef1234567890"

    color_array = [choice(color_strings) for a in range(6)]
    final_string = "#"
    for a in color_array:
        final_string += a

    return final_string

while True:
    x = [a for a in range(10**3)]
    y = [randint(10**2, 10**5) for a in range(10**3)]

    colors = [random_color() for a in range(10**3)]
    size = [randint(1,50) for a in range(10**3)]

    plt.scatter(x, y, c=colors, s=size)

    plt.show()