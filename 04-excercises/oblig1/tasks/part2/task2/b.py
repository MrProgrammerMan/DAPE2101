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

t = np.linspace(0, 7, 100)

x_a = R * np.cos(w * t + 3*np.pi/2)
y_a = R * np.sin(w * t + 3*np.pi/2)

x_b = -w * (h - R) * t
y_b = h - R + 6 * t

plt.figure()
plt.plot(x_a, y_a, label=r"$\vec{r}_a$")
plt.plot(x_b, y_b, label=r"$\vec{r}_b$")

plt.gca().set_title(r"$\vec{r}_a$ og $\vec{r}_b$ for $t\in[0, 7]$")
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.tight_layout()

plt.savefig("b.pgf")
plt.close()