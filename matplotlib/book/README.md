# Matplotlib
## Line Plot
### Basic Code
```python
import matplotlib.pyplot as plt

x = [a for a in range(5)]
y = [a for a in range(5)]

plt.plot(x, y)
plt.show()
```

### Trigonometry plot
- The function `numpy.sin()`, `numpy.cos()`, and `numpy.tan()` are used to calculate values for trigonometric functions
```python
import matplotlib.pyplot as plt
import numpy as np

vals = np.arange(0,10,0.1)

a = np.sin(vals)
b = np.cos(vals)
c = np.tan(vals)

plt.plot(vals,a)
plt.plot(vals,b)
plt.plot(vals,c)

plt.show()
```

### Line Width
- Line width is controlled by the `linewidth` argument of `plot()` function

```python
import matplotlib.pyplot as plt
import random

x = [random.randint(1,10) for a in range(10)]
y = [a for a in range(10)]

plt.plot(x,y, linewidth=random.randint(5,100))
plt.show()
```

### Change line color
- `color` argument of `plot()` function is used to change the line color in a line plot of matplotlib function

```python
import matplotlib.pyplot as plt
import random

x = [random.randint(1,10) for a in range(10)]
y = [a for a in range(10)]

plt.plot(x,y, color="#aaaaaa")
plt.show()
```

### Change line style
- `linestyle` parameter of `plot()` function is used for changing the line style

Possible values for line style:-
| Representation | Name |
| -------------- | ---- |
| : | Dotted |
| -. | Dash Dot |
| -- | Dashed |
| - | Solid |

```python
import matplotlib.pyplot as plt
import random

possible_linestyles = [':', "-.", "--", "-"]
## equal to dotted, dashdot, dashed, solid

x = [random.randint(1,10) for a in range(10)]
y = [a for a in range(10)]

plt.plot(x,y, linestyle=random.choice(possible_linestyles))
plt.show()
```

### Marker Style
- It can be controlled by `marker` parameter of `plot()` function
- Possible values for marker style:-

| Marker | Description        |
|--------|--------------------|
| 'o'    | Circle             |
| 's'    | Square             |
| '^'    | Triangle (up)      |
| 'v'    | Triangle (down)    |
| '<'    | Triangle (left)    |
| '>'    | Triangle (right)   |
| 'x'    | X marker           |
| '+'    | Plus marker        |
| '*'    | Asterisk marker    |
| 'D'    | Diamond            |
| 'd'    | Thin diamond       |
| 'p'    | Pentagon           |
| 'H'    | Hexagon (horizontal) |
| 'h'    | Hexagon (vertical) |
| '1'    | Tri down marker    |
| '2'    | Tri up marker      |
| '3'    | Tri left marker    |
| '4'    | Tri right marker   |
| '.'    | Point marker       |
| ','    | Pixel marker       |
| 'None' | No marker          |

```python
import matplotlib.pyplot as plt
from random import randint

size = 10

x = [randint(5,15) for a in range(size)]
y = [a for a in range(size)]

plt.plot(x, y, marker="<")

plt.show()
```

## Scatter plot
- This can be done using two functions
    - plot()
    - scatter()

### Basic Code
- **Using `plot()` function**
```python
import matplotlib.pyplot as plt

x = [a for a in range(5)]
y = [a for a in range(5)]

plt.plot(x, y, 'o')

plt.show()
```

- **Using `scatter()` function**
```python
import matplotlib.pyplot as plt

x = [a for a in range(5)]
y = [a for a in range(5)]

plt.scatter(x, y)

plt.show()
```

### Scatter marker types
- This can be done using `marker` argument of `scatter()` function.

```python
import matplotlib.pyplot as plt

x = [a for a in range(10)]
y = [a for a in range(10)]

plt.scatter(x, y, marker="x")

plt.show()
```

- **Marker Types:-**
| Marker | Description        |
|--------|--------------------|
| '.'    | Point marker       |
| ','    | Pixel marker       |
| 'o'    | Circle             |
| 'v'    | Triangle (down)    |
| '^'    | Triangle (up)      |
| '<'    | Triangle (left)    |
| '>'    | Triangle (right)   |
| 's'    | Square             |
| 'p'    | Pentagon           |
| '*'    | Star               |
| 'h'    | Hexagon1           |
| 'H'    | Hexagon2           |
| '+'    | Plus               |
| 'x'    | X marker           |
| 'D'    | Diamond            |
| 'd'    | Thin diamond       |
| '|'    | Vline              |

### Size of marker
- This can be done using the `s` argument of `scatter()` function
    - **NOTICE that it is `s` and NOT `size`**

```python
import matplotlib.pyplot as plt

x = [a for a in range(5)]
y = [a for a in range(5)]

plt.scatter(x, y, s=1)
plt.show()
```

### Color of marker
- This can be specified using the `c` argument of `scatter()` function

```python
import matplotlib.pyplot as plt

x = [a for a in range(10)]
y = [a for a in range(10)]

plt.plot(x, y, c='#aaaaaa')

plt.show()
```

## Bar plot
### Simple Plot
- This can be done using the `bar()` function

```python
import matplotlib.pyplot as plt

x = [a for a in range(100)]
y = [a for a in range(50)] + [a for a in range(50, 0, -1)]
plt.bar(x,y)

plt.show()
```

### Horizontal Plot
- This can be done using `barh()` function

```python
import matplotlib.pyplot as plt

x = [a for a in range(100)]
y = [a for a in range(100)]

plt.barh(x,y)

plt.show()
```