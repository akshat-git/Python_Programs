import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1 - x)
n = 10000
r = np.linspace(2.5, 4.0, n)
iterations = 1000
last = 100
x = 1e-5 * np.ones(n)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 9),sharex=True)
for i in range(iterations):

    x = logistic(r, x)
    # We display the bifurcation diagram.
    if i >= (iterations - last):
        plt.plot(r, x, ',k', alpha=.25)
        print("-")
plt.set_xlim(2.5, 4)
ax1.set_title("Bifurcation diagram")
