import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "font.family": "serif",
    "text.usetex": True,
    "pgf.rcfonts": False,
})

C  = 1.735e-21   # J
l0 = 2.36e-10    # m

# Lennard-Jones potensial
def Ep(r):
    return C * ((l0/r)**12 - (l0/r)**6)

# intervall
r = np.linspace(2e-10, 5e-10, 1000)
energy = Ep(r)

# Bindingslengde analytisk: R0 = 2^(1/6) * l0
R0 = 2**(1/6) * l0
Ep0 = Ep(R0)

fig, ax = plt.subplots(figsize=(6, 4))

# Grafen
ax.plot(r * 1e10, energy * 1e21, color="steelblue", linewidth=1.8, label=r"$E_p(r)$")

# Marker R_0
ax.scatter([R0 * 1e10], [Ep0 * 1e21], color="crimson", zorder=5, label=rf"Energi: $E_p0 = {Ep0*1e21:.3f}$")

# Asymptote
ax.axhline(0, color="gray", linestyle="--", linewidth=0.8, label=r"$E_p \to 0$")

ax.set_ylim(-1, 3.5) # Bare vis nyttige deler av grafen

ax.set_xlabel(r"Avstand $r$ [\AA]")
ax.set_ylabel(r"Potensiell energi $E_p$ [$10^{-21}$ J]")
ax.set_title(r"Lennard--Jones-potensial for argon")
ax.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.savefig("e.pgf")
plt.close()