import numpy as np
import matplotlib.pyplot as plt


def logistic_equation(r, x):
    return r * x * (1 - x)


def logistic_map():
    n = 10000  # number of points in R-dimension
    r_start, r_end = 2.5, 4.0
    r = np.linspace(r_start, r_end, n)  # generate points on R axis
    no_iter = 1000  # number of iterations
    last_iter = 50  # higher number -> more dense logistic map
    x = 1e-5 * np.ones(n)  # initial values of population X

    for i in range(no_iter):
        x = logistic_equation(r, x)
        if i >= (no_iter - last_iter):
            # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
            plt.plot(r, x, ",k", alpha=.25)  # draw as black pixels ",k"

    plt.title("Logistic map")
    plt.xlabel("growth rate: r")
    plt.xlim(r_start, r_end)
    plt.ylabel("ratio of population: x")
    plt.ylim(0.0, 1.0)
    plt.tight_layout()
    plt.show()


logistic_map()
