import matplotlib.pyplot as plt

time = [12, 14, 16, 18, 20, 22]

game_a = [1500, 1800, 2400, 3200, 4100, 3900]
game_b = [1200, 1600, 2100, 3500, 4300, 4000]

plt.plot(time, game_a, label="Игра А", color="blue", linestyle="-")
plt.plot(time, game_b, label="Игра В", color="green", linestyle="--")

plt.title("Онлайн в двух играх в разное время")
plt.xlabel("Время")
plt.ylabel("Игроки")
plt.grid()
plt.legend()

plt.show()

# В 17 часов Игра В впервые обогнала Игру А
