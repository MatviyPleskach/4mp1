import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

x = np.linspace(0.5, 1.5)
y = np.linspace(0.6, 0.5)


ax.plot(x, y)
ax.grid()
plt.title("---")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
