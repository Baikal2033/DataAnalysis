import matplotlib.pyplot as plt

size = [10, 25, 50, 75, 100, 150, 200]
time = [2, 5, 9, 14, 20, 31, 45]

plt.plot(size, time, marker="o")

plt.title("Время загрузки файлов")
plt.xlabel("Размер файла, МБ")
plt.ylabel("Время загрузки, сек")
plt.grid()

plt.show()

# Время загрузки файла увеличивается при его росте в весе
# Завмсимость не похожа на линейный рост
