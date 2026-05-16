import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 15)
temperature = [12, 15, 9, 20, 18, 25, 22, 16, 14, 19, 24, 28, 26, 30]

plt.plot(days, temperature, marker="o")

plt.title("Прочитанные страницы")
plt.xlabel("День")
plt.ylabel("Страницы")
plt.grid()

plt.tight_layout()
plt.show()

# К концу периода ученик стал читать больше
