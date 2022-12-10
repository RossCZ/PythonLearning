import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R


def cone_fn(x, y, height_ratio=2):
    """Parametric function of a cone."""
    a, b = height_ratio, height_ratio
    return np.sqrt(a ** 2 * x ** 2 + b ** 2 * y ** 2)


def generate_circular_grid(radius):
    """Generates circular XY grid of given radius."""
    r = np.linspace(0, radius, num=300)
    theta = np.linspace(0, 2 * np.pi, num=300)
    radius_matrix, theta_matrix = np.meshgrid(r, theta)

    X = radius_matrix * np.cos(theta_matrix)
    Y = radius_matrix * np.sin(theta_matrix)
    return X, Y


def generate_cone_points(r, h):
    """Generates cone points of a cone with radius r and height h"""
    X, Y = generate_circular_grid(r)
    Z = cone_fn(X, Y, h / r)
    A = np.stack((X, Y, Z), axis=2) #.reshape(-1, 3)  # stack X, Y, and Z arrays  # shape size 3 or 2
    return A


def cut_zero(cone_points):
    """Removes (invalidates) points where Z < 0."""
    def cut_zero_fn(pnt):
        pnt[2] = np.nan if pnt[2] < 0.0 else pnt[2]
        return pnt
    return np.apply_along_axis(cut_zero_fn, axis=2, arr=cone_points)


def transform(cone_points, degrees=0, move=0):
    """Rotate (around X) and translate (in Z) cone points."""
    def move_fn(pnt):
        pnt[2] += move
        return pnt

    rmatrix = R.from_euler("x", degrees, degrees=True).as_matrix()
    tvector = np.array([0, 0, move])

    # apply rotation to each point of the cone using the rotation matrix and translation vector
    transform_fn = lambda pnt: np.dot(rmatrix, pnt) + tvector
    cone_points = np.apply_along_axis(transform_fn, axis=2, arr=cone_points)
    return cone_points


def visualize(cone_points):
    """Visualize cone points in 3D plot."""
    X = cone_points.take(indices=0, axis=2)
    Y = cone_points.take(indices=1, axis=2)
    Z = cone_points.take(indices=2, axis=2)

    # # plot 2D representation - deve
    # plt.scatter(X, Y)
    # plt.show()

    ax = plt.axes(projection="3d")

    # ax.plot(*cone_points.reshape(-1, 3).T, lw=0.5)
    ax.plot_surface(X, Y, Z, cmap="viridis")
    # ax.plot_trisurf(X.flatten(), Y.flatten(), Z.flatten(), cmap="magma")
    ax.set_title("Conic section")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_box_aspect([1, 1, 1])
    plt.show()


def conic_section_example():
    # https://en.wikipedia.org/wiki/Conic_section
    cone_points = generate_cone_points(r=6, h=12)  # shape(theta_split, radius_split, xyz_coordinates)
    cone_points = transform(cone_points, degrees=42, move=-3)
    cone_points = cut_zero(cone_points)
    visualize(cone_points)


if __name__ == "__main__":
    conic_section_example()
