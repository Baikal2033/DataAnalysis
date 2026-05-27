import matplotlib.pyplot as plt
import numpy as np

categories = ["Яблоко", "Банан", "Апельсин", "Груша", "Киви"]
np.random.seed(42)
numbers = np.random.randint(1, 10, size=5)

plt.pie(numbers, labels=categories, autopct="%1.1f%%")

plt.title("Количество голосов за любимые фрукты")

plt.tight_layout()
plt.show()
