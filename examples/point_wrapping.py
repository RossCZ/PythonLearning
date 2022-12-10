import matplotlib.pyplot as plt
import numpy as np


def point_wrapping_example(no_points, show_probing=True):
    all_points = np.random.rand(no_points, 2)  # generate N points in 2D plane
    points_to_probe = list(all_points)

    left_most_point_index = np.argmin(all_points[:, 0])  # starting point is the left-most point
    hull = [all_points[left_most_point_index]]  # convex hull points

    plt.plot(all_points[:, 0], all_points[:, 1], "kx", label="points")  # format: [marker][line][color]  # https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.pyplot.plot.html
    plt.plot(*hull[0], "bo", label="hull")
    plt.title("Point wrapping algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.tight_layout()
    plt.legend()

    while True:
        next_index = 0
        next_vertex = points_to_probe[next_index]

        for index, probed_vertex in enumerate(points_to_probe):
            # calculate the cross product of two vectors: for 2D plane returns Z value of 3D cross product
            # if the probed point lies counter-clockwise of the next_vertex, it replaces it
            if np.cross(next_vertex - hull[-1], probed_vertex - hull[-1]) > 0:
                next_vertex = probed_vertex
                next_index = index

            # show probing of the next hull segment
            if show_probing and len(hull) == 2:
                plt.plot((hull[-1][0], probed_vertex[0]), (hull[-1][1], probed_vertex[1]), "k-", linewidth=0.5)
                plt.pause(0.1)

        # add next vertex to the hull
        hull.append(points_to_probe[next_index])
        points_to_probe.pop(next_index)  # hull point don't need additional probing (except the first one to close the hull)

        # show the last hull segment
        plt.plot((hull[-2][0], hull[-1][0]), (hull[-2][1], hull[-1][1]), "b-", marker=".")
        plt.pause(0.1)

        # the hull is closed
        if np.all(hull[-1] == hull[0]):
            print("Done!")
            hull_np = np.array(hull)
            plt.gca().fill(hull_np.take(indices=0, axis=1), hull_np.take(indices=1, axis=1), color="b", alpha=0.1)
            break

    plt.show()


if __name__ == "__main__":
    # https://en.wikipedia.org/wiki/Gift_wrapping_algorithm
    point_wrapping_example(no_points=30, show_probing=True)
