import pandas as pd
import os

# Путь к папке с файлом
FOLDER_PATH = r"C:\123\машинное обучение\практика 6\Lab6.1"
file_path = os.path.join(FOLDER_PATH, "megaGymDataset.csv")

# a) Считываем содержимое файла в DataFrame
df = pd.read_csv(file_path)

# b) 5 упражнений с максимальным рейтингом
top5_rating = df.nlargest(5, 'Rating')
print("Топ-5 упражнений по рейтингу:")
print(top5_rating[['Title', 'Rating']])  # для наглядности выводим название и рейтинг
print()

# c) 3 упражнения с минимальным рейтингом
bottom3_rating = df.nsmallest(3, 'Rating')
print("Топ-3 упражнений с наименьшим рейтингом:")
print(bottom3_rating[['Title', 'Rating']])
print()

# d) Упражнения с оборудованием "Cable"
cable_exercises = df.query("Equipment == 'Cable'")
print("Упражнения с оборудованием Cable (первые 5 строк для примера):")
print(cable_exercises[['Title', 'Equipment']].head())
print(f"Всего найдено: {len(cable_exercises)}")
print()

# e) Упражнения типа "Cardio" для уровня "Beginner"
cardio_beginner = df.query("Type == 'Cardio' and Level == 'Beginner'")
print("Упражнения типа Cardio для начинающих (первые 5 строк):")
print(cardio_beginner[['Title', 'Type', 'Level']].head())
print(f"Всего найдено: {len(cardio_beginner)}")
print()

# f) Уникальные значения в столбце "Type"
unique_types = df['Type'].unique()
print("Уникальные типы упражнений:")
print(unique_types)
