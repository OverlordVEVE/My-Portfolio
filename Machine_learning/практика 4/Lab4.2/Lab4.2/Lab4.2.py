import pandas as pd
import os

# Путь к папке с файлом
FOLDER_PATH = r"C:\123\машинное обучение\практика 4\Lab4.2"
input_file = os.path.join(FOLDER_PATH, "Cities.xlsx")
output_file = os.path.join(FOLDER_PATH, "Cities_modified.xlsx")  # новый файл

# a) Считываем содержимое исходного файла
df = pd.read_excel(input_file)
print("Исходные данные (первые 5 строк):")
print(df.head(), "\n")

# b) Города с населением более 1 млн человек
df_large_cities = df.loc[df['Population'] > 1_000_000]
print("Города с населением > 1 млн:")
print(df_large_cities, "\n")

# c) Города с площадью более 1000 кв. км
df_large_area = df.loc[df['Area'] > 1000]
print("Города с площадью > 1000 км²:")
print(df_large_area, "\n")

# d) Города на высоте менее 100 м над уровнем моря
df_low_elevation = df.loc[df['Elevation'] < 100]
print("Города с высотой < 100 м:")
print(df_low_elevation, "\n")

# e) Увеличить население Казани на 2 человека с помощью iloc
kazan_mask = df['City'] == 'Kazan'
if kazan_mask.any():
    kazan_row_idx = df[kazan_mask].index[0]
    pos = df.index.get_loc(kazan_row_idx)
    pop_col_pos = df.columns.get_loc('Population')
    old_value = df.iloc[pos, pop_col_pos]
    df.iloc[pos, pop_col_pos] += 2
    print(f"Население Казани увеличено на 2: {old_value} -> {df.iloc[pos, pop_col_pos]}\n")
else:
    print("Город 'Kazan' не найден!\n")

# f) Увеличить площадь Екатеринбурга на 1,5 кв. км с помощью loc
ekb_mask = df['City'] == 'Ekaterinburg'
if ekb_mask.any():
    old_area = df.loc[ekb_mask, 'Area'].values[0]
    df.loc[ekb_mask, 'Area'] += 1.5
    new_area = df.loc[ekb_mask, 'Area'].values[0]
    print(f"Площадь Екатеринбурга увеличена на 1.5 км²: {old_area} -> {new_area}\n")
else:
    print("Город 'Ekaterinburg' не найден!\n")

# g) Увеличить значение в столбце Elevation для Сочи на 1 с помощью iloc
sochi_mask = df['City'] == 'Sochi'
if sochi_mask.any():
    sochi_row_idx = df[sochi_mask].index[0]
    pos_s = df.index.get_loc(sochi_row_idx)
    elev_col_pos = df.columns.get_loc('Elevation')
    old_elev = df.iloc[pos_s, elev_col_pos]
    df.iloc[pos_s, elev_col_pos] += 1
    print(f"Высота Сочи увеличена на 1 м: {old_elev} -> {df.iloc[pos_s, elev_col_pos]}\n")
else:
    print("Город 'Sochi' не найден!\n")

# Итоговые данные после изменений
print("Итоговые данные после всех изменений:")
print(df)

# Сохраняем изменения в НОВЫЙ файл, исходный остаётся без изменений
df.to_excel(output_file, index=False)
print(f"Изменения сохранены в новый файл: {output_file}")
