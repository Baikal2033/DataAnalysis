import matplotlib.pyplot as plt

change = [1, 2, 3, 4, 5, 6]

tea = [12, 18, 25, 20, 15, 10]
cacao = [8, 15, 20, 24, 22, 16]

plt.plot(change, tea, label="Чай", color="blue", linestyle="-")
plt.plot(change, cacao, label="Какао", color="green", linestyle="--")

plt.title("Продажи в школьном буфете")
plt.xlabel("Перемена")
plt.ylabel("Кол-во")
plt.grid()
plt.legend()

plt.show()

# На 3 перемене продали больше всего чая
# На 4 перемене продали больше всего какао
# С 4 по 6 перемену какао продавалось лучше чая
