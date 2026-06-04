import pandas as pd
import os
import matplotlib.pyplot as plt

# Путь к папке с файлами
FOLDER_PATH = r"C:\123\машинное обучение\практика 6\Lab6.2"
file_path = os.path.join(FOLDER_PATH, "sleep_health_lifestyle_dataset.csv")

# a) Считываем содержимое файла
df = pd.read_csv(file_path)
print("Файл загружен. Размер таблицы:", df.shape)

# b) Проверка наличия дубликатов
duplicates_count = df.duplicated().sum()
print(f"Количество строк-дубликатов: {duplicates_count}")

# c) Фильтрация с помощью isin и loc (просто вывод количества, данные не сохраняем)
categories = ["Underweight", "Normal"]
filtered = df.loc[(df["BMI Category"].isin(categories)) & (df["Occupation"] == "Student")]
print(f"Количество строк, где BMI категория в {categories} и Occupation = 'Student': {len(filtered)}")

# d) Создание нового столбца с категориями сна
bins = [0, 7, 9, 24]
labels = ["insufficient", "adequate", "excessive"]
df["Sleep_duration_str"] = pd.cut(df["Sleep Duration (hours)"], bins=bins, labels=labels, right=False)

# e) Создание столбца с категориями качества сна через qcut
# Используем qcut с обработкой возможных дубликатов на границах
df["Sleep_quality_str"] = pd.qcut(df["Quality of Sleep (scale: 1-10)"],
                                   q=3,
                                   labels=["low", "medium", "high"],
                                   duplicates='drop')
print("\nРаспределение по категориям качества сна:")
print(df["Sleep_quality_str"].value_counts())

# f) Кодирование столбца BMI Category целыми числами
# Создаём словарь: каждой уникальной категории присваиваем номер
unique_bmi = df["BMI Category"].unique()
bmi_mapping = {cat: i+1 for i, cat in enumerate(unique_bmi)}  # нумерация с 1
df["BMI_num"] = df["BMI Category"].map(bmi_mapping)
print("Соответствие категорий BMI и чисел:", bmi_mapping)

# g) Бинаризация столбца Occupation с drop_first=True
occupation_dummies = pd.get_dummies(df["Occupation"],
                                    prefix="Occupation",
                                    drop_first=True,
                                    dtype='int64')
df = pd.concat([df, occupation_dummies], axis=1)
print(f"Добавлено {occupation_dummies.shape[1]} дамми-переменных для Occupation")

# h) Построение гистограммы для столбца Quality of Sleep
plt.figure(figsize=(10, 6))
df["Quality of Sleep (scale: 1-10)"].plot.hist(bins=15, edgecolor='black', alpha=0.7)
plt.title("Распределение качества сна (шкала 1-10)")
plt.xlabel("Качество сна")
plt.ylabel("Частота")
plt.grid(axis='y', alpha=0.3)
plt.show()

# Сохраняем итоговый DataFrame в Excel
output_file = os.path.join(FOLDER_PATH, "sleep_health_lifestyle_updated.xlsx")
df.to_excel(output_file, index=False)
print(f"\nФайл со всеми изменениями сохранён как: {output_file}")
