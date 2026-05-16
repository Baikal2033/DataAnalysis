import matplotlib.pyplot as plt

categories = ["Сон", "Школа", "Домашние задания", "Отдых", "Хобби", "Дорога"]
expenses = [8, 6, 3, 4, 2, 1]

plt.pie(expenses, labels=categories, autopct="%1.1f%%")

plt.title("Распределение времяни в течение дня")

plt.tight_layout()
plt.show()

# 37.5 процентов времяни заняла учеба
# Диаграмму удобно читать
