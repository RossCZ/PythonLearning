import matplotlib.pyplot as plt
import numpy as np


def visualize_iteration_metrics(iter_x, diffs):
    fig, ax = plt.subplots(figsize=(12, 5))
    plt.title("Iteration metrics")
    ax2 = ax.twinx()
    ax.plot(iter_x, label="x value")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("X value")
    ax2.set_yscale("log")
    ax2.plot(diffs, color="orange", label="diff")
    ax2.set_ylabel("Diff")
    ax.grid()
    ax.legend(loc="upper center")
    ax2.legend(loc="upper right")
    plt.tight_layout()
    plt.show()


def visualize_iteration(x_start, x_end, fn1, fn2, iter_x, iter_y):
    y_fn1, y_fn2 = [], []
    x_vals = np.linspace(x_start, x_end, 1000)
    for x in x_vals:
        y_fn1.append(fn1(x))
        y_fn2.append(fn2(x))

    plt.title("Iteration process")
    plt.plot(x_vals, y_fn1, label="fn1")
    plt.plot(x_vals, y_fn2, label="fn2")
    plt.scatter(iter_x, iter_y, color="red", marker="o")
    for i, x in enumerate(iter_x):
        plt.annotate(i + 1, (x, iter_y[i]))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    # plt.grid()
    plt.tight_layout()
    plt.show()


def bisection_example():
    # define two functions to find intersection
    fn1 = lambda x: 0.5 * x ** 3 - 8 * x ** 2 - 3 * x + 50 * np.sin(x)
    fn2 = lambda x: 80 * x - 660

    # iteration parameters
    tol = 1e-4
    x_start, x_end = 0, 20
    bnd_low, bnd_high = x_start, x_end
    diff = float("inf")

    # bisection iteration
    iter_x, iter_y, diffs = [], [], []
    cnt = 0
    while abs(diff) > tol:
        cnt += 1
        if cnt > 50:
            break
        # calculate x and difference
        x = (bnd_low + bnd_high) / 2
        diff = fn1(x) - fn2(x)

        # update boundaries
        if diff > 0:
            bnd_low = x
        else:
            bnd_high = x

        # log values
        iter_x.append(x)
        iter_y.append(fn1(x))
        diffs.append(abs(diff))
        print(f"\tIteration: {len(iter_x)}, x: {x}, diff: {diff}")

    print(f"Bisection finished in {len(iter_x)} steps. The result is: {iter_x[-1]}")
    visualize_iteration_metrics(iter_x, diffs)
    visualize_iteration(x_start, x_end, fn1, fn2, iter_x, iter_y)


bisection_example()
