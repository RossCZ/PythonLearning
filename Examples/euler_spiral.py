import math
from matplotlib import pyplot as plt


def calculate_euler_spiral():
    l_tot = 500.0  # m
    l_step = 0.1  # m
    R = 100.0  # m

    A2 = l_tot * R
    A = math.sqrt(l_tot * R)

    print(f"A2: {A2}")

    x_coords, y_coords = [0], [0]
    x_coords2, y_coords2 = [0], [0]
    l, x, y = 0, 0, 0

    while l < l_tot:
        # https://etrr.springeropen.com/articles/10.1007/s12544-013-0119-8
        x += l_step * math.cos(l ** 2 / (2 * A2))
        y += l_step * math.sin(l ** 2 / (2 * A2))
        x_coords.append(x)
        y_coords.append(y)

        l += l_step

        # only for engineering purposes (not returning clothoid (e.g. R = 100 m))
        x2 = l - l ** 5 / (40 * A ** 4) + l ** 9 / (3456 * A ** 8) - l ** 13 / (599040 * A ** 12)
        y2 = l ** 3 / (6 * A ** 2) - l ** 7 / (336 * A ** 6) + l ** 11 / (42240 * A ** 10)
        x_coords2.append(x2)
        y_coords2.append(y2)

    plt.plot(x_coords, y_coords, color="blue")
    plt.plot(x_coords2, y_coords2, color="red")
    plt.show()


calculate_euler_spiral()
