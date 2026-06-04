import pandas as pd
import ast
import os

# Путь к папке с файлом
FOLDER_PATH = r"C:\123\машинное обучение\практика 5\Lab5.2"
csv_file = os.path.join(FOLDER_PATH, "lowest_ranked_movies_data.csv")
excel_file = os.path.join(FOLDER_PATH, "lowest_ranked_movies_data2.xlsx")
processed_file = os.path.join(FOLDER_PATH, "lowest_ranked_movies_processed.xlsx")

# a) Чтение CSV-файла
df_csv = pd.read_csv(csv_file, encoding='utf-8')
print("CSV-файл прочитан. Размер:", df_csv.shape)

# Сохранение в Excel (расстановка по столбцам)
df_csv.to_excel(excel_file, sheet_name='Movies', index=False)
print(f"Создан Excel-файл: {excel_file}")

# Теперь работаем с созданным Excel-файлом
df = pd.read_excel(excel_file, sheet_name=0)
print("Данные из Excel загружены. Размер:", df.shape)
print("Столбцы:", list(df.columns))

# Функция безопасного извлечения первого элемента из строки-списка
def get_first_item(cell):
    if pd.isna(cell):
        return ''
    try:
        # Преобразуем строку в список с помощью ast.literal_eval
        items = ast.literal_eval(cell)
        if isinstance(items, list) and len(items) > 0:
            return str(items[0]).strip()
        else:
            return ''
    except (ValueError, SyntaxError):
        # В случае ошибки парсинга возвращаем пустую строку
        return ''

# b) Создание столбца с главным актёром (первый в списке stars)
df['lead_actor'] = df['stars'].apply(get_first_item)
print("b) Столбец 'lead_actor' создан.")

# c) Создание столбца с основным жанром (первый в списке genre)
df['main_genre'] = df['genre'].apply(get_first_item)
print("c) Столбец 'main_genre' создан.")

# d) Проверка новых столбцов на наличие апострофов и их удаление
# Проверяем, есть ли символ "'" в любом значении столбцов
apost_in_actor = df['lead_actor'].astype(str).str.contains("'", na=False).any()
apost_in_genre = df['main_genre'].astype(str).str.contains("'", na=False).any()

if apost_in_actor or apost_in_genre:
    print("d) Найдены апострофы. Выполняем замену...")
    df['lead_actor'] = df['lead_actor'].astype(str).str.replace("'", "", regex=False)
    df['main_genre'] = df['main_genre'].astype(str).str.replace("'", "", regex=False)
    print("   Замена завершена.")
else:
    print("d) Апострофы не обнаружены.")

# e) Подсчёт фильмов с сертификацией "Not Rated"
# Столбец certification может содержать пропуски, обрабатываем их
not_rated_mask = df['certification'].astype(str).str.contains('Not Rated', case=False, na=False)
not_rated_count = not_rated_mask.sum()
print(f"e) Количество фильмов с сертификацией 'Not Rated': {not_rated_count}")

# f) Самое длинное название фильма (столбец 'name')
# Преобразуем к строке на случай пропусков
title_lengths = df['name'].astype(str).str.len()
max_len = title_lengths.max()
longest_movie = df.loc[title_lengths == max_len, 'name'].iloc[0]
print(f"f) Самое длинное название ({max_len} симв.): {longest_movie}")

# Сохранение обработанного DataFrame в новый файл
df.to_excel(processed_file, sheet_name='Movies', index=False)
print(f"Сохранён новый файл: {processed_file}")
