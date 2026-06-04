import pandas as pd
import os

# Путь к папке с файлами (используем тот же, что и в предыдущих заданиях)
FOLDER_PATH = r"C:\123\машинное обучение\практика 6\Lab6.4"
file_path = os.path.join(FOLDER_PATH, "sleep_health_lifestyle_dataset.csv")

# a) Считываем содержимое файла
df = pd.read_csv(file_path)
print("Данные загружены. Размер таблицы:", df.shape)
print("Первые 5 строк:")
print(df.head())

# b) Сводная таблица: средняя продолжительность сна в разрезе пола и типа занятости
pivot_sleep = pd.pivot_table(
    df,
    values='Sleep Duration (hours)',
    index='Gender',
    columns='Occupation',
    aggfunc='mean'
)
print("\nСредняя продолжительность сна (часы) по полу и занятости:")
print(pivot_sleep)

# c) Кросс-таблица: частотность сочетаний пола и типа занятости
crosstab_gender_occup = pd.crosstab(index=df['Gender'], columns=df['Occupation'])
print("\nКросс-таблица (пол × занятость) – количество людей:")
print(crosstab_gender_occup)

# d) Сводная таблица: минимальное количество шагов в день в разрезе категории ИМТ и пола
pivot_steps = pd.pivot_table(
    df,
    values='Daily Steps',
    index='BMI Category',
    columns='Gender',
    aggfunc='min'
)
print("\nМинимальное количество шагов по категории ИМТ и полу:")
print(pivot_steps)


pivot_sleep.to_excel(os.path.join(FOLDER_PATH, "pivot_sleep.xlsx"))
crosstab_gender_occup.to_excel(os.path.join(FOLDER_PATH, "crosstab.xlsx"))
pivot_steps.to_excel(os.path.join(FOLDER_PATH, "pivot_steps.xlsx"))
