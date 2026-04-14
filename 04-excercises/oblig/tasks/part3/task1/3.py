import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "font.family": "serif",
    "text.usetex": True,
    "pgf.rcfonts": False,
})

start = 0
end = 2*60*60 # 2 timer i sekunder
granularity = 1000 # antall datapunkter
dt = (end - start) / granularity
T4 = 293.15**4 # Lufttemp T^4
h = 10
A = 2.545e-2
c = 800
m = 1.031

def dT(T, k):
    return -h*A/(c*m)*(T-293.15)-k*(T**4-T4)

fig, ax = plt.subplots(figsize=(6, 4))

k = 1.575e-12
ts = np.linspace(start, end, granularity)
T = 400 + 273.15 # Kelvin
vals = []
for t in ts:
    vals.append(T-273.15)
    T+=dT(T, k) * dt

ax.plot(ts, vals, color='steelblue', linewidth=1.8, label=r"Stein uten folie")

k = 5.249e-14
ts = np.linspace(start, end, granularity)
T = 400 + 273.15 # Kelvin
vals = []
for t in ts:
    vals.append(T-273.15)
    T+=dT(T, k) * dt

ax.plot(ts, vals, color='crimson', linewidth=1.8, label=r"Stein med folie")

ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)

ax.set_xlim(start, end)
ax.set_ylim(0, 425)

ax.set_xlabel(r"Tid $t$ [s]")
ax.set_ylabel(r"Temperatur $T$ [$^\circ$C]")
ax.set_title(r"Temperaturen av steinene over 2 timer med konveksjon")
ax.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.savefig("3.pgf")
plt.close()