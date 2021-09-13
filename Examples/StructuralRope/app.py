import math
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
# import numpy as np


class Node:
    def __init__(self, m, x, y):
        self.m = m  # kg
        self.x = x  # m
        self.y = y  # m
        self.vx = 0.0  # m/s
        self.vy = 0.0  # m/s


class Rope:
    def __init__(self, lines, step, length, no_nodes, k, g, weight_per_length, damping):
        self.lines = lines
        self.step = step  # s
        self.k = k  # stiffness: k = F/l [N/m]
        self.g = g  # m/s2
        self.c = damping  # kg/s
        self.no_nodes = no_nodes

        self.d = length / (self.no_nodes - 1)  # initial segment length [m]
        node_weight = weight_per_length * self.d

        self.nodes = []
        for n in range(self.no_nodes):
            self.nodes.append(Node(node_weight, self.d * n, 0.0))

    def calculate_spring_forces(self, node, index_next_node):
        Fx, Fy = 0.0, 0.0

        # if next node exists
        if 0 <= index_next_node < self.no_nodes:
            node_next = self.nodes[index_next_node]

            # segment distance
            dx = node.x - node_next.x
            dy = node.y - node_next.y
            dist = math.sqrt(dx ** 2 + dy ** 2)

            # spring forces in X and Y direction
            Fx = self.k * (self.d - dist) * dx / dist
            Fy = self.k * (self.d - dist) * dy / dist

        return Fx, Fy

    def simulate_step(self, visualize):
        x_difs, y_difs = [], []
        vx_difs, vy_difs = [], []

        for i in range(self.no_nodes):
            # support nodes (start and end node
            if i == 0 or i == (self.no_nodes - 1):
                x_difs.append(0)
                y_difs.append(0)
                vx_difs.append(0)
                vy_difs.append(0)
                continue

            # current node
            node = self.nodes[i]

            # left spring forces
            FxL, FyL = self.calculate_spring_forces(node, i - 1)

            # right spring forces
            FxR, FyR = self.calculate_spring_forces(node, i + 1)

            # node acceleration + gravitational force in Y direction
            ax = (FxL + FxR - self.c * node.vx) / node.m
            ay = (FyL + FyR + node.m * self.g - self.c * node.vy) / node.m

            # speed differences
            vx_difs.append(ax * self.step)
            vy_difs.append(ay * self.step)

            # coordinates differences
            x_difs.append(node.vx * self.step + 0.5 * ax * (self.step ** 2))
            y_difs.append(node.vy * self.step + 0.5 * ay * (self.step ** 2))

        # update coordinates and speed of the nodes
        for i, node in enumerate(self.nodes):
            node.x += x_difs[i]
            node.y += y_difs[i]
            node.vx += vx_difs[i]
            node.vy += vy_difs[i]

        if visualize:
            return self.visualize()

    def visualize(self):
        x, y = [], []
        off = []

        for node in self.nodes:
            x.append(node.x)
            y.append(node.y)

        self.lines.set_data(x, y)
        # self.lines.set_offsets(np.column_stack((x, y)))  # update position of scatter plot
        return self.lines,
            

def run_simulation():
    fig = plt.figure(figsize=[6, 4])
    ax = plt.axes(xlim=(0, 100), ylim=(-70, 0.0))
    # ax.axis('off')
    # points = ax.scatter([], [], color="blue", s=3, edgecolors=None)
    lines, = ax.plot([], [], color="blue", linewidth=1)

    rope = Rope(lines, step=0.001, length=100.0, no_nodes=50, k=5e2, g=-9.81, weight_per_length=1.0, damping=0.4)

    # Animation
    def animate(i):
        # skip animation every n-th step
        for i in range(100):
            rope.simulate_step(False)
        return rope.simulate_step(True)

    anim = FuncAnimation(fig, animate, frames=200, interval=1, blit=True)
    plt.show()
    # anim.save('animation.gif', fps=30, dpi=200)


run_simulation()
