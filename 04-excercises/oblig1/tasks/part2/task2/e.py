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

# Regn ut posisjonene i kartesisk
x_a = R * np.cos(w * t + 3*np.pi/2)
y_a = R * np.sin(w * t + 3*np.pi/2)

x_b = -w * (h - R) * t
y_b = h - R + 6 * t

# Konverter til polar
r_a = np.sqrt(x_a**2 + y_a**2)
theta_a = np.arctan2(y_a, x_a)

r_b = np.sqrt(x_b**2 + y_b**2)
theta_b = np.arctan2(y_b, x_b)

t_f = 1.306772601
idx = np.abs(t - t_f).argmin() # Shenanigans for a plukke ut et punkt som er utregnet neare t_f

# Punkter til astronauten og ballen ved t=T_f
r_a_point = r_a[idx]
theta_a_point = theta_a[idx]
r_b_point = r_b[idx]
theta_b_point = theta_b[idx]

plt.figure()
ax = plt.subplot(111, polar=True)

ax.plot(theta_a, r_a, label=r"$\vec{r}_a$")
ax.plot(theta_b, r_b, label=r"$\vec{r}_b$")

ax.scatter(theta_a_point, r_a_point, color='blue', s=50, zorder=5)
ax.scatter(theta_b_point, r_b_point, color='red', s=50, zorder=5)

plt.text(theta_a_point + 0.5, r_a_point + 0.5, r"$a$ ved $T_f$", color='blue')
plt.text(theta_b_point + 0.5, r_b_point + 0.5, r"$b$ ved $T_f$", color='red')

ax.set_title(r"Polarplott av $\vec{r}_a$ og $\vec{r}_b$ for $t\in[0, 3]$")
ax.grid(True)
ax.legend()

plt.tight_layout()

plt.savefig("e.pgf")
plt.close()