import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.animation import FuncAnimation


class Simulator:
    def __init__(self, ax, rows, columns, seeds, diffusion_ratios, diffusion_speed, as_source=False):
        self.rows = rows  # number of rows in the matrix
        self.columns = columns  # number of columns in the matrix
        self.diffusion_ratios = diffusion_ratios  # up, down, left, right (must sum to 100 %)
        self.diffusion_speed = diffusion_speed  # speed of diffusion
        self.as_source = as_source  # if seeds are endless source of substance or not

        self.matrix = np.zeros([rows, columns])
        # regular vs. normalized colormap
        # self.im = ax.imshow(self.matrix, cmap="plasma", vmin=0.0, vmax=1.0)
        # self.im = ax.imshow(self.matrix, cmap="plasma", norm=colors.LogNorm(1e-9, 1.0))
        self.im = ax.imshow(self.matrix, cmap="plasma", norm=colors.PowerNorm(gamma=0.1, vmin=0.0, vmax=1.0))

        # initialize diffusion seeds
        for s in range(seeds):
            self.matrix[random.randint(0, self.rows - 1), random.randint(0, self.columns - 1)] = 1.0

    def simulate_step(self):
        matrix_temp = np.zeros([self.rows, self.columns])
        for row in range(self.rows):
            for col in range(self.columns):
                neighbour_values = []
                if row > 0:  # up
                    neighbour_values.append(self.diffusion_ratios[0] * self.matrix[row - 1, col])
                if row < self.rows - 1:  # down
                    neighbour_values.append(self.diffusion_ratios[1] * self.matrix[row + 1, col])
                if col > 0:  # left
                    neighbour_values.append(self.diffusion_ratios[2] * self.matrix[row, col - 1])
                if col < self.columns - 1:  # right
                    neighbour_values.append(self.diffusion_ratios[3] * self.matrix[row, col + 1])

                # calculate new value from this and neighbouring concentrations
                orig_multiplier = 1.0 if self.as_source else (1.0 - self.diffusion_speed)
                matrix_temp[row, col] = orig_multiplier * self.matrix[row, col] + self.diffusion_speed * np.sum(neighbour_values)

        # update matrix and return animation data
        self.matrix = matrix_temp
        self.im.set_data(self.matrix)
        return [self.im]


def simulate_diffusion():
    fig = plt.figure(figsize=[8, 6])
    ax = plt.axes()
    ax.axis('off')

    simulator = Simulator(ax, rows=50, columns=80, seeds=8, diffusion_ratios=[0.17, 0.28, 0.34, 0.31], diffusion_speed=0.1, as_source=False)

    # Animation
    def animate(i):
        return simulator.simulate_step()

    anim = FuncAnimation(fig, animate, frames=50, interval=10, blit=True)
    fig.colorbar(simulator.im, fraction=0.03, pad=0.04)
    plt.show()
    # anim.save('diffusion.gif', fps=30, dpi=200)


simulate_diffusion()

