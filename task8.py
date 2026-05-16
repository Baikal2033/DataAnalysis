import matplotlib.pyplot as plt

categories = ["Сок", "Булочка", "Пицца", "Сэндвич", "Печенье"]
expenses = [45, 25, 60, 35, 15]
explode = [0, 0, 0.04, 0, 0.1]

plt.pie(expenses, labels=categories, autopct="%1.1f%%", explode=explode)

plt.title("Продажа товаров в магазине")

plt.tight_layout()
plt.show()

# Если нужно узнать какой товар продавался больше всего а какой меньше всего
# то лучше использовать столбчатую диаграмму
