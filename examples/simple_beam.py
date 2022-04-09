from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt


class Beam():
    def __init__(self, length, name=""):
        self.name = name
        self.length = length
        self.forces = OrderedDict()  # key: x [m], value: Fz [kN]
        self.internal_V = [], []
        self.internal_M = [], []

    def add_force(self, x, magnitude):
        if x <= 0 or x >= self.length:
            return

        if x not in self.forces.keys():
            self.forces[x] = magnitude
        else:
            self.forces[x] += magnitude
        self.forces = OrderedDict(sorted(self.forces.items()))  # sort forces by keys

    def calculate_reactions(self):
        # sum M at 1 = 0: 0 = sum(x * mag) + r2 * length
        R2 = -np.sum([x * mag for x, mag in self.forces.items()]) / self.length
        # sum Fz = 0: 0 = sum(x * mag) + r1 + r2
        R1 = -(np.sum(list(self.forces.values())) + R2)
        return R1, R2

    def __append_next_V(self, x, F):
        # calculated from left, get previous V if it exists
        V_prev = 0
        if len(self.internal_V[1]) > 0:
            V_prev = self.internal_V[1][len(self.internal_V[1]) - 1]
        # print(f"{x}: previous V: {V_prev}")
        self.internal_V[0].append(x)
        self.internal_V[1].append(V_prev)

        # change of V
        self.internal_V[0].append(x)
        self.internal_V[1].append(V_prev + F)

    def __append_next_M(self, x, R1):
        # calculated from left - reaction R1 must be known
        mom = x * R1

        # any forces on the left applicable to the moment calculation at this X
        for x_left, mag_left in self.forces.items():
            if x_left > x:
                break
            mom += (x - x_left) * mag_left

        self.internal_M[0].append(x)
        self.internal_M[1].append(-mom)  # opposite sign

    def calculate_V(self):
        # calculated from the left to right
        self.internal_V = [], []  # reset old values

        # reactions
        R1, R2 = self.calculate_reactions()
        self.__append_next_V(0, R1)

        # forces on the beam
        for x, mag in self.forces.items():
            self.__append_next_V(x, mag)

        # reaction 2
        self.__append_next_V(self.length, R2)

    def calculate_M(self):
        # calculated from the left to right
        self.internal_M = [], []  # reset old values

        # reactions
        R1, R2 = self.calculate_reactions()
        self.__append_next_M(0, R1)

        # forces on the beam
        for x, mag in self.forces.items():
            self.__append_next_M(x, R1)

        self.__append_next_M(self.length, R1)

    def visualize(self):
        # calculate internal forces
        self.calculate_V()
        self.calculate_M()

        plt.title(f"Simple beam {self.name} - internal forces")
        plt.plot(self.internal_V[0], self.internal_V[1], color="blue", label="V [kN]")
        plt.plot(self.internal_M[0], self.internal_M[1], color="red", label="M [kNm]")
        plt.plot([0, self.length], [0, 0], color="black", label="beam", linewidth=3, marker="o", markersize=8, markerfacecolor="white")

        def add_arrow(x, arrow_size, color, label=""):
            plt.arrow(x, -arrow_size, 0, arrow_size, color=color, width=0.05, head_length=1.5, length_includes_head=True, label=label)

        arr_scale = 2.0
        for i, (x, mag) in enumerate(self.forces.items()):
            add_arrow(x, mag * arr_scale, "green", "forces" if i == 0 else "")
        R1, R2 = self.calculate_reactions()
        add_arrow(0, R1 * arr_scale, "orange", "reactions")
        add_arrow(self.length, R2 * arr_scale, "orange")

        plt.xlabel("x [m]")
        plt.ylabel("internal force value")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()


def example():
    # beam instance 1
    beam = Beam(10, "id 1")
    beam.add_force(2, -5)
    beam.add_force(6, -8)
    # print(beam.forces)
    # print(beam.calculate_reactions())
    # beam.calculate_V()  # change object internal state
    # print(beam.internal_V)
    beam.visualize()

    # beam instance 2
    beam2 = Beam(8, "id 2")
    beam2.add_force(4, -10)
    for x in np.linspace(0, 8, 30):
        beam2.add_force(x, -1)
    beam2.visualize()


example()
