import pandas as pd

# Путь к папке с файлом
FOLDER_PATH = r"C:\123\машинное обучение\практика 5\Lab5.1"
input_file = f"{FOLDER_PATH}\\Movies.xlsx"

# a) Чтение файла
df = pd.read_excel(input_file, sheet_name=0)
print("Данные загружены. Размер таблицы:", df.shape)

# b) Фильмы, снятые в Великобритании (полностью или частично)
uk_mask = df['country'].str.contains('Great Britain', case=False, na=False)
uk_count = uk_mask.sum()
print(f"b) Фильмов, связанных с Великобританией: {uk_count}")

# c) Количество фильмов Кристофера Нолана
nolan_mask = df['directed_by'].str.contains('Christopher Nolan', case=False, na=False)
nolan_count = nolan_mask.sum()
print(f"c) Кристофер Нолан был режиссёром {nolan_count} раз(а)")

# d) Доля фильмов в жанре "science fiction"
sf_mask = df['genre'].str.contains('science fiction', case=False, na=False)
sf_share = sf_mask.sum() / len(df) * 100
print(f"d) Доля фильмов с жанром 'science fiction': {sf_share:.2f}%")

# e) Создание столбца с фамилиями режиссёров
df['director_lastname'] = df['directed_by'].apply(lambda x: str(x).split()[-1] if pd.notna(x) else '')
print("e) Столбец с фамилиями добавлен.")

# f) Режиссёр с наибольшим количеством букв 'm'
# Приводим к нижнему регистру для регистронезависимого подсчёта
m_count = df['directed_by'].str.lower().str.count('m')
max_m = m_count.max()
director_max_m = df.loc[m_count == max_m, 'directed_by'].iloc[0]
print(f"f) Режиссёр с наибольшим числом букв 'm' ({max_m}): {director_max_m}")

# g) Режиссёр с минимальной длиной имени
name_length = df['directed_by'].str.len()
min_len = name_length.min()
director_min_len = df.loc[name_length == min_len, 'directed_by'].iloc[0]
print(f"g) Режиссёр с минимальной длиной имени ({min_len} симв.): {director_min_len}")

# Сохранение копии файла с новым столбцом
output_file = f"{FOLDER_PATH}\\Movies_with_director_lastname.xlsx"
df.to_excel(output_file, sheet_name='Movies', index=False)
print(f"Сохранён новый файл: {output_file}")
