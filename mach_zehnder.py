import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# Define beam splitter matrix
BS1 = np.array([[-1/np.sqrt(2), 1/np.sqrt(2)], [1/np.sqrt(2), 1/np.sqrt(2)]])
BS2 = np.array([[1/np.sqrt(2), 1/np.sqrt(2)], [1/np.sqrt(2), -1/np.sqrt(2)]])

# Initial angle and state vector (using global keyword for modification)
initial_angle = 0
initial_state = np.array([np.cos(initial_angle), np.sin(initial_angle)])

# Calculate state vectors (using global keyword for modification)
state_after_bs1 = BS1 @ initial_state
state_after_bs2 = BS2 @ state_after_bs1

# Function to update the plot
def update(val):
    global initial_state, state_after_bs1, state_after_bs2, initial_angle
    initial_angle = angle_slider.val  # Get angle from slider
    initial_state = np.array([np.cos(initial_angle), np.sin(initial_angle)]) # Recalculate using rotation

    state_after_bs1 = BS1 @ initial_state
    state_after_bs2 = BS2 @ state_after_bs1

    line1.set_data([0, initial_state[0]], [0, initial_state[1]])
    line2.set_data([0, state_after_bs1[0]], [0, state_after_bs1[1]])
    line3.set_data([0, state_after_bs2[0]], [0, state_after_bs2[1]])

    fig.canvas.draw_idle()

# Create the figure and axes
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.35)

ax.set_xlabel("|H>")
ax.set_ylabel("|V>")
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal')
ax.set_title("Mach-Zehnder Interferometer")
ax.grid(color='0.9', linestyle='-', linewidth=1)

# Initialize lines (CORRECTED)
line1, = ax.plot([0, initial_state[0]], [0, initial_state[1]], color="blue", label="Initial")
line2, = ax.plot([0, state_after_bs1[0]], [0, state_after_bs1[1]], color="green", label="After BS1")
line3, = ax.plot([0, state_after_bs2[0]], [0, state_after_bs2[1]], color="red", label="After BS2")

ax.legend()

# Create angle slider (with limits)
axcolor = 'lightgoldenrodyellow'
angle_slider_ax = fig.add_axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

min_angle = 0
max_angle = 2 * np.pi
angle_slider = Slider(angle_slider_ax, 'Initial Angle (rad)', min_angle, max_angle, valinit=initial_angle)

angle_slider.on_changed(update)

plt.show()