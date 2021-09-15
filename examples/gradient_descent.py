import numpy as np
import matplotlib.pyplot as plt


def fn1(x):
    return x ** 2


# or using autograd module
def fn1_grad(x):
    return 2 * x


def sgd(gradient, x_init, step_size, n_iter):
    points = [x_init]
    for _ in range(n_iter):
        diff = -step_size * gradient(points[-1])
        points.append(points[-1] + diff)
    return points


def gradient_descent_example():
    x = np.linspace(-10, 10, 100)
    y = list(map(fn1, x))

    x_res = sgd(fn1_grad, 6, 0.8, 10)
    y_res = list(map(fn1, x_res))

    plt.plot(x, y, color="grey")
    plt.plot(x_res, y_res, color="red", marker="o", markersize=3)
    plt.show()


gradient_descent_example()
