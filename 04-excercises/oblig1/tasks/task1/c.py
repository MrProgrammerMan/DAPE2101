import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "font.family": "serif",
    "text.usetex": True,
    "pgf.rcfonts": False,
})

x = np.linspace(-5, 5, 400)
y = x**2

plt.figure()
plt.plot(x, y, label=r"$x^2$")
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.legend()
plt.tight_layout()

plt.savefig("c.pgf")
plt.close()