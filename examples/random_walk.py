import numpy as np
import matplotlib.pyplot as plt


def random_walk():
    # parameters
    steps = 1000
    step_size = 0.1

    # initialize x and y arrays
    x = np.linspace(0, steps, steps)
    y = []

    for i in range(steps):
        if i == 0:
            y.append(0)
        else:
            # calculate next value based on previous value and random difference
            y.append(y[-1] + np.sin(np.random.uniform(0, 1) * np.pi - np.pi / 2) * step_size)

    ylim = max(abs(min(y)), max(y)) * 1.1
    plt.ylim(-ylim, ylim)
    plt.plot(x, y)
    plt.show()


random_walk()
