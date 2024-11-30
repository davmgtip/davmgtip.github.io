import matplotlib.pyplot as plt
import random

color_names = '123546789abcdef'

def random_color():
    color_list = [random.choice(color_names) for a in range(6)]

    color = "#"
    for x in color_list:
        color += x

    random.choice(color_names)

while True:
    try:
        color_list = [random.choice(color_names) for a in range(6)]

        color = "#"
        for x in color_list:
            color += x

        random.choice(color_names)

        x = [random.randint(1,10000) for a in range(5)]
        y = [random.randint(1,10000) for a in range(5)]

        plt.xlabel("jo bhi hai")
        plt.ylabel('kuch aur')

        plt.plot(x,y, color=color, linewidth=5)

        plt.show()
    except KeyboardInterrupt:
        break

# while True:
#     try:
#         color_list = [random.choice(color_names) for a in range(6)]

#         color = "#"
#         for x in color_list:
#             color += x

#         random.choice(color_names)

#         x = [random.randint(1,10000) for a in range(5)]
#         y = [random.randint(1,10000) for a in range(5)]

#         plt.hist(x, color=color)

#         plt.show()
#     except KeyboardInterrupt:
#         break


# while True:
#     try:
#         color_list = [random.choice(color_names) for a in range(6)]

#         color = "#"
#         for x in color_list:
#             color += x

#         random.choice(color_names)

#         x = [a for a in range(100)]
#         y = [random.randint(1,10000) for a in range(100)]

#         plt.bar(x,y,color=color)

#         plt.show()
#     except KeyboardInterrupt:
#         break