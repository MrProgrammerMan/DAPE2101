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

t = np.linspace(0, 3, 100)

x_a = R * np.cos(w * t + 3*np.pi/2)
y_a = R * np.sin(w * t + 3*np.pi/2)

x_b = 12.95 * t
y_b = h - R + 6 * t

r_a = np.sqrt(x_a**2 + y_a**2)
theta_a = np.arctan2(y_a, x_a)

r_b = np.sqrt(x_b**2 + y_b**2)
theta_b = np.arctan2(y_b, x_b)

t_point = 1.306772601
idx = np.abs(t - t_point).argmin()  # closest index in t

r_a_point = r_a[idx]
theta_a_point = theta_a[idx]
r_b_point = r_b[idx]
theta_b_point = theta_b[idx]

plt.figure()
ax = plt.subplot(111, polar=True)

ax.plot(theta_a, r_a, label=r"$\vec{r}_a$")
ax.plot(theta_b, r_b, label=r"$\vec{r}_b$")

ax.scatter(theta_a_point, r_a_point, color='blue', s=50, zorder=5,
           label=r"$t={:.2f}$ for $\vec{{r}}_a$".format(t_point))
ax.scatter(theta_b_point, r_b_point, color='red', s=50, zorder=5,
           label=r"$t={:.2f}$ for $\vec{{r}}_b$".format(t_point))

ax.set_title(r"Polarplott av $\vec{r}_a$ og $\vec{r}_b$ for $t\in[0, 3]$")
ax.grid(True)
ax.legend()

plt.tight_layout()

plt.savefig("e.pgf")
plt.close()