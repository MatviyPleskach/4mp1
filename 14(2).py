import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()


x1 = np.linspace(1.4, 2.4)
y2 = np.linspace(2.5, 4.2)

ax.plot(x1, y2)
ax.grid()
plt.title('---')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
