import numpy as np
import matplotlib.pyplot as plt


def structural_rope_example():
    # given: either rope length or horizontal reaction
    # coordinate system:
    # o-->  (+x)
    # |
    # v (+z)

    # settings
    Rxb = 2000  # [N]  # horizontal reaction at the second support
    zb = 1  # [m]  # z coordinate of the second support
    dx = 10  # [m]  # distance between supports in x direction

    forces = [  # (Fzi, xi)
        (600, 2),
        (650, 5),
        (250, 8),
    ]
    # forces = [(10, x) for x in np.linspace(0, dx, 1000)]

    # *** CALCULATION
    # reactions
    moments = [Fzi * xi for Fzi, xi in forces]
    forces_z = [Fzi for Fzi, xi in forces]
    Rzb = (Rxb * zb - np.sum(moments)) / dx
    Rza = -(np.sum(forces_z) + Rzb)

    # add reaction to the forces list
    forces.insert(0, (Rza, 0))
    forces.append((Rzb, dx))
    # print(forces)

    # rope shape (segments from the left)
    xi, zi = [0], [0]
    Nzi = 0
    for i in range(1, len(forces)):
        Nzi -= forces[i - 1][0]
        dxi = forces[i][1] - forces[i - 1][1]
        dzi = dxi * Nzi / Rxb  # dzi/Nzi == dxi/Nxi (Nxi==Rxb==const)
        # print(dxi, dzi, Nzi)
        xi.append(xi[-1] + dxi)
        zi.append(zi[-1] + dzi)

    # visualize
    plt.title("Structural rope")
    plt.plot(xi, zi, marker="o")
    plt.gca().invert_yaxis()
    plt.grid()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    structural_rope_example()
