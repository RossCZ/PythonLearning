import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(x, y, threshold):
    # Calculates if the number c = x + i*y belongs to the Mandelbrot set.
    # Sequence z[i + 1] = z[i]**2 + c must not diverge after threshold number of steps.
    limit = 2.

    # initial conditions
    c = complex(x, y)
    z = complex(0, 0)

    # number diverged after certain number of steps?
    for i in range(threshold):
        z = z ** 2 + c
        if abs(z) > limit:
            return i

    return threshold - 1


def mandelbrot_example():
    # initial parameters
    x_start, y_start = -2.0, -1.3
    width, height = 3.0, 2.6
    density = 300
    threshold = 20  # [1;n]

    # values of real and imaginary axis
    real = np.linspace(x_start, x_start + width, int(width * density))
    imaginary = np.linspace(y_start, y_start + height, int(height * density))

    # generate points
    X = np.empty((len(real), len(imaginary)))
    print(f"number of pixels: {len(X.flatten())}")
    for r in range(len(real)):
        for i in range(len(imaginary)):
            X[r, i] = mandelbrot(real[r], imaginary[i], threshold)

    # visualize
    # fig = plt.figure(frameon=False)
    plt.imshow(X.T, interpolation="gaussian", cmap="inferno")  # aspect="auto"
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    mandelbrot_example()
