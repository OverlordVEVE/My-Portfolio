import pandas as pd
import ast
import os

# Путь к папке с файлами
FOLDER_PATH = r"C:\123\машинное обучение\практика 6\Lab6.3"
file_path = os.path.join(FOLDER_PATH, "lowest_ranked_movies_data.csv")

# a) Считываем содержимое файла
df = pd.read_csv(file_path)
print("Файл загружен. Размер таблицы:", df.shape)
print("Столбцы в файле:", df.columns.tolist())  # <-- посмотрим имена

# b) Количество пропусков по каждому столбцу
missing = df.isna().sum()
print("Пропуски по столбцам:")
print(missing)

# c) Проверка наличия строк-дубликатов
duplicates = df.duplicated().sum()
print(f"Количество строк-дубликатов: {duplicates}")

# d) Преобразование столбца stars с помощью ast.literal_eval
df['stars'] = df['stars'].apply(ast.literal_eval)
print("Столбец 'stars' преобразован в списки.")

# Сохраняем промежуточный результат
intermediate_file = os.path.join(FOLDER_PATH, "lowest_ranked_movies_stars_parsed.xlsx")
df.to_excel(intermediate_file, index=False)
print(f"Промежуточный файл сохранён: {intermediate_file}")

# e) Разворачиваем списки актеров в отдельные строки
df_exploded = df.explode('stars').reset_index(drop=True)
print("Таблица после explode (первые 5 строк):")
print(df_exploded.head())  # <-- выводим всё, чтобы увидеть названия столбцов

# f) Топ-10 актеров
top_actors = df_exploded['stars'].value_counts().head(10)
print("Топ-10 актеров, наиболее часто снимавшихся в фильмах с низким рейтингом:")
print(top_actors)

# Сохраняем explode
exploded_file = os.path.join(FOLDER_PATH, "lowest_ranked_movies_exploded.xlsx")
df_exploded.to_excel(exploded_file, index=False)
print(f"Файл с развернутыми актерами сохранён: {exploded_file}")


