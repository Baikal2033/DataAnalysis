import pandas as pd

data = {
    "Товар": ["Клавиатура", "Мышь", "Тетрадь", "Ручка", "Наушники"],
    "Категория": ["техника", "техника", "канцелярия", "канцелярия", "техника"],
    "Цена": [2500, 1200, 80, 40, 3200],
    "Количество": [12, 20, 100, 150, 8]
}


df = pd.DataFrame(data)


print(df)
print(df["Цена"].max())
print(df["Цена"].min())
print(df["Цена"].mean())
print(df["Количество"].sum())
print(df["Цена"].count())
print(df["Категория"].value_counts())
print(df.describe())
