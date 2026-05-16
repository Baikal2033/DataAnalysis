import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 4, 100)
y = x ** 3

plt.plot(x, y)

plt.title("График y = x^3")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

plt.tight_layout()
plt.show()
