import matplotlib.pyplot as plt
import numpy as np
import warnings
P=np.linspace(2.5,4,400000)
m=0.7

X = []
Y = []
warnings.filterwarnings("ignore")
for u in P:
    X.append(u)
    m = np.random.random()
    for n in range(100):
        m=(u*m)*(1-m)
    for l in range(100):
        m=(u*m)*(1-m)
    for n in range(100):
        m=(u*m)*(1-m)
    for l in range(100):
        m=(u*m)*(1-m)
    Y.append(abs(m))
plt.plot(X, Y, ls='', marker=',',markersize=0.01)
plt.show()
