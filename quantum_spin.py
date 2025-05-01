import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# Pauli matrices
sigma_x = np.array([[0, 1], [1, 0]])
sigma_y = np.array([[0, -1j], [1j, 0]])
sigma_z = np.array([[1, 0], [0, -1]])

# Calculate eigenvectors using linalg
eigenvalues_x, eigenvectors_x = np.linalg.eig(sigma_x)
eigenvalues_y, eigenvectors_y = np.linalg.eig(sigma_y)
eigenvalues_z, eigenvectors_z = np.linalg.eig(sigma_z)

# Function to calculate the state vector components and spin projections
def get_state_vector(theta):

    """Calculates the state vector components based on the given angle."""

    state_vector = np.array([np.cos(theta / 2), np.sin(theta / 2)])

    # Project the state vector onto the eigenvectors of the Pauli matrices.
    # Important:  Use the *squared magnitude* of the projections to get probabilities.
    x_projections = np.array([np.abs(np.dot(state_vector, eigenvectors_x[:, 0]))**2,
                             np.abs(np.dot(state_vector, eigenvectors_x[:, 1]))**2])
    y_projections = np.array([np.abs(np.dot(state_vector, eigenvectors_y[:, 0]))**2,
                             np.abs(np.dot(state_vector, eigenvectors_y[:, 1]))**2])
    z_projections = np.array([np.abs(np.dot(state_vector, eigenvectors_z[:, 0]))**2,
                             np.abs(np.dot(state_vector, eigenvectors_z[:, 1]))**2])
    return state_vector, x_projections, y_projections, z_projections

# Function to update the plot and calculations
def update(val):

    """Updates the plot and calculations based on the slider value."""
    
    theta = slider.val
    state_vector, x_projections, y_projections, z_projections = get_state_vector(theta)

    # Update the vector in the complex plane plot
    line.set_data([0, state_vector[0]], [0, state_vector[1]])

    # Update the text labels to show the projections (probabilities)
    x_coord_text.set_text(f"P(+x): {x_projections[0]:.2f}\nP(-x): {x_projections[1]:.2f}")
    y_coord_text.set_text(f"P(+y): {y_projections[0]:.2f}\nP(-y): {y_projections[1]:.2f}")
    z_coord_text.set_text(f"P(+z): {z_projections[0]:.2f}\nP(-z): {z_projections[1]:.2f}")
    state_vector_text.set_text(f"|ψ> = [{state_vector[0]:.2f}, {state_vector[1]:.2f}]")
    state_vector_text.set_position((state_vector[0], state_vector[1]))

    # Redraw the plot
    fig.canvas.draw_idle()

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim([-1.2, 1.2])
ax.set_ylim([-1.2, 1.2])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('State Vector for Spin -1/2 Quantum Particles')
ax.grid(True)

# Plot the axes
ax.plot([0, 1], [0, 0], 'k-', label='X Axis')
ax.plot([0, 0], [0, 1], 'k-', label='Y Axis')

# Eigenvectors of sigma_x
ax.plot([0, eigenvectors_x[0, 0].real], [0, eigenvectors_x[1, 0].real], 'b-', linewidth=1, label='|+x>')
ax.plot([0, eigenvectors_x[0, 1].real], [0, eigenvectors_x[1, 1].real], 'b-', linewidth=1, label='|-x>')
# Eigenvectors of sigma_z
ax.plot([0, eigenvectors_z[0, 0].real], [0, eigenvectors_z[1, 0].real], 'r-', linewidth=1, label='|+z>')
ax.plot([0, eigenvectors_z[0, 1].real], [0, eigenvectors_z[1, 1].real], 'r-', linewidth=1, label='|-z>')

# Initial state vector
initial_theta = 0
initial_state_vector, x_projections, y_projections, z_projections = get_state_vector(initial_theta)
line, = ax.plot([0, initial_state_vector[0]], [0, initial_state_vector[1]], 'r-', linewidth=2, label='State Vector')

# Add text labels for the spin coordinates, showing *probabilities*
x_coord_text = ax.text(1.2, 0.8, f"P(+x): {x_projections[0]:.2f}\nP(-x): {x_projections[1]:.2f}", transform=ax.transAxes, ha='left')
y_coord_text = ax.text(1.2, 0.7, f"P(+y): {y_projections[0]:.2f}\nP(-y): {y_projections[1]:.2f}", transform=ax.transAxes, ha='left')
z_coord_text = ax.text(1.2, 0.6, f"P(+z): {z_projections[0]:.2f}\nP(-z): {z_projections[1]:.2f}", transform=ax.transAxes, ha='left')
state_vector_text = ax.text(initial_state_vector[0], initial_state_vector[1],
                            f"|ψ> = [{initial_state_vector[0]:.2f}, {initial_state_vector[1]:.2f}]",
                            ha='center', va='bottom')

# Add a slider for theta
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Theta', -2 * np.pi, 2 * np.pi, valinit=initial_theta)
slider.on_changed(update)

# Add legend
ax.legend(loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()
