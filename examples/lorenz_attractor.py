import numpy as np
import matplotlib.pyplot as plt


def lorenz(x, y, z, s=10, r=28, b=2.667):
    """Calculates next point of Lorenz attractor given the previous position and specified parameters."""
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return np.array([x_dot, y_dot, z_dot])


def generate_lorenz_points(dt, n):
    lorenz_points = np.empty((n + 1, 3))
    lorenz_points[0] = (0.1, 0.2, 0.3)  # initial position
    # calculate partial derivatives at the current point from the previous position
    for i in range(n):
        lorenz_points[i + 1] = lorenz_points[i] + lorenz(*lorenz_points[i]) * dt
    return lorenz_points


def visualize(lorenz_points):
    ax = plt.axes(projection="3d", facecolor="black")
    ax.set_axis_off()
    ax.set_frame_on(False)
    plt.gcf().set_size_inches(8, 8)
    plt.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)

    cmap = plt.cm.winter
    # plot each segment with different color
    for i in range(0, lorenz_points.shape[0] - 1):
        x = lorenz_points[i:i+2].take(indices=0, axis=1)
        y = lorenz_points[i:i+2].take(indices=1, axis=1)
        z = lorenz_points[i:i+2].take(indices=2, axis=1)
        ax.plot(x, y, z, color=cmap(i / lorenz_points.shape[0]), linewidth=0.8, alpha=0.5)  # draw segment between two points
        # ax.plot(*lorenz_points[i].T, markersize=0.4, marker="o", color=cmap(i / lorenz_points.shape[0]), alpha=0.6)  # draw point

    plt.show()


def lorenz_attractor_example():
    lorenz_points = generate_lorenz_points(dt=0.01, n=10000)
    visualize(lorenz_points)


if __name__ == "__main__":
    # https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html
    lorenz_attractor_example()
