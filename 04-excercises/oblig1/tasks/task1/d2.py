import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "font.family": "serif",
    "text.usetex": True,
    "pgf.rcfonts": False,
})

w=.7
R=20
h=1.5

t = np.linspace(0, 2, 100)

x_a = R * np.cos(w * t + 3*np.pi/2)
y_a = R * np.sin(w * t + 3*np.pi/2)

x_b = 12.95 * t
y_b = h - R + 6 * t

t_point = 1.306772601
x_a_point = R * np.cos(w * t_point + 3*np.pi/2)
y_a_point = R * np.sin(w * t_point + 3*np.pi/2)
x_b_point = 12.95 * t_point
y_b_point = h - R + 6 * t_point

plt.figure()
plt.plot(x_a, y_a, label=r"$\vec{r}_a$")
plt.plot(x_b, y_b, label=r"$\vec{r}_b$")

plt.scatter(x_a_point, y_a_point, color='blue', zorder=5)
plt.scatter(x_b_point, y_b_point, color='red', zorder=5)

plt.text(x_a_point + 0.5, y_a_point + 0.5, r"$a$ at $t\approx1.3$", color='blue')
plt.text(x_b_point + 0.5, y_b_point + 0.5, r"$b$ at $t\approx1.3$", color='red')

plt.gca().set_title(r"$\vec{r}_a$ og $\vec{r}_b$ for $t\in[0, 2]$")
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.tight_layout()

plt.savefig("d2.pgf")
plt.close()