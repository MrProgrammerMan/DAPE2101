import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "font.family": "serif",
    "text.usetex": True,
    "pgf.rcfonts": False,
})

C = 1.735e-21   # J
l0 = 2.36e-10   # m

r = np.linspace(2.5e-10, 5e-10, 1000)

F = C * (-12 * l0**12 / r**13 + 6 * l0**6 / r**7)

plt.figure()
plt.plot(r * 1e10, F * 1e12, color='steelblue')

plt.axhline(y=0, color='gray', linestyle='-', linewidth=0.8)

plt.ylim(-10, 10)

plt.gca().set_title(r"Lennard-Jones-kraft fra det ene argon-atomet til det andre")
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
plt.xlabel(r"$r$ [\AA]")
plt.ylabel(r"$F$ [pN]")
plt.tight_layout()

plt.savefig("c.pgf")
plt.close()