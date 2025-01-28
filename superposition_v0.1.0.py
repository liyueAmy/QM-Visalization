import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

class VectorAnimator:
    def __init__(self, ax, a):
        self.ax = ax
        self.paused = False
        self.time = 0
        self.dt = 0.01
        self.speed = 1.0
        self.a = a

    def generate_vector(self, t):
        # Calculate b using Born Rule (assuming |a|^2 + |b|^2 = 1)
        b = np.sqrt(1 - np.abs(self.a)**2)  # Ensure b is real and positive
        # Calculate angle using complex argument
        angle = np.angle(self.a)
        # Calculate vector components
        x = np.real(self.a * np.exp(1j * angle))
        y = np.imag(self.a * np.exp(1j * angle))
        return x, y

    def generate_frames(self, num_frames=100):
        frames = []
        for _ in range(num_frames):
            if not self.paused:
                self.time += self.dt * self.speed
            x, y = self.generate_vector(self.time)
            arrow = self.ax.arrow(0, 0, x, y, head_width=0.1, head_length=0.15, fc='r', ec='k')
            frames.append([arrow])
        return frames

if __name__ == "__main__":
    # Get input for a (complex number)
    a_str = input("Enter the value of a (complex number, e.g., 0.5+0.5j): ")
    a = complex(a_str)

    fig, ax = plt.subplots()
    ax.set_xlim(0, 1.5)
    ax.set_ylim(0, 1.5)
    ax.grid(True)

    animator = VectorAnimator(ax, a)
    frames = animator.generate_frames()

    anim = ArtistAnimation(fig, frames, interval=10)
    plt.show()