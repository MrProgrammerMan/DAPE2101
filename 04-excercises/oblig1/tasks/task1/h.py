import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "font.family": "serif",
    "text.usetex": True,
    "pgf.rcfonts": False,
})

a = 9.81
h = 1.5
R_values = [20, 200, 2000, 6000000]

t = np.linspace(0, 2, 100)

plt.figure()

for R in R_values:
    w = np.sqrt(a / R)
    
    x_a = R * np.cos(w * t + 3*np.pi/2)
    y_a = R * np.sin(w * t + 3*np.pi/2)
    
    x_b = -w * (h - R) * t
    y_b = h - R + 6 * t
    
    theta_a = np.arctan2(y_a, x_a)
    
    x_b_ref = -np.sin(theta_a)*(x_b - x_a) + np.cos(theta_a)*(y_b - y_a)
    y_b_ref = -np.cos(theta_a)*(x_b - x_a) - np.sin(theta_a)*(y_b - y_a)
    
    plt.plot(x_b_ref, y_b_ref, label=f'R = {R}')

plt.plot(0, 0, 'ro', label='Astronaut')

plt.title(r"Ballens bevegelse fra astronautens perspektiv for $t \in [0, 2]$ for forskjellige verdier av R")
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.legend()
plt.tight_layout()

plt.savefig("h.pgf")
plt.close()