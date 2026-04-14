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
t_point = 1.306772601

x_a = R * np.cos(w * t + 3*np.pi/2)
y_a = R * np.sin(w * t + 3*np.pi/2)

x_b = -w * (h - R) * t
y_b = h - R + 6 * t

# Avstanden i vektorform
dist_x = x_a - x_b
dist_y = y_a - y_b

# Absolutt avstand
dist = np.sqrt(dist_x**2 + dist_y**2)

dist_point = np.sqrt((R * np.cos(w * t_point + 3*np.pi/2) - 12.95 * t_point)**2 +
                     (R * np.sin(w * t_point + 3*np.pi/2) - (h - R + 6 * t_point))**2)

plt.figure()
plt.plot(t, dist)

plt.axvline(x=t_point, color='red', linestyle='--', linewidth=1, label=r"$t_\mathrm{point}$")

plt.scatter([t_point], [dist_point], color='blue', zorder=5)

plt.annotate(
    f"({t_point:.2f}, {dist_point:.2f})", 
    xy=(t_point, dist_point), 
    xytext=(t_point + 0.1, dist_point + 1),
    arrowprops=dict(arrowstyle="->", color='black'),
    fontsize=10
)

plt.gca().set_title(r"Avstand mellom A og B for tiden $t \in [0, 2]$")
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
plt.xlabel(r"$t$")
plt.ylabel(r"$avstand$")
plt.legend()
plt.tight_layout()

plt.savefig("f.pgf")
plt.close()