import matplotlib.pyplot as plt

fb_series = [0,1]
nFib = 500

for x in range(nFib):
    next_num = int(fb_series[-1]) + int(fb_series[-2])
    fb_series.append(next_num)

y_axis = [a for a in range((nFib+2))]

plt.plot(y_axis, fb_series)
plt.show()