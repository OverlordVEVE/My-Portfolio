import pandas as pd
import os

# Путь к папке с файлом
FOLDER_PATH = r"C:\123\машинное обучение\практика 4\Lab4.1"
file_path = os.path.join(FOLDER_PATH, "Simple_table.xlsx")

# a) Считываем содержимое файла
df = pd.read_excel(file_path)

print("Исходный DataFrame:")
print(df)
print("\n" + "="*50 + "\n")

# b) С использованием атрибута loc изменяем значения в последних двух строках столбца "Discount"
last_two_indices = df.index[-2:]
df.loc[last_two_indices, "Discount"] = [0.1, 0.15]

# c) С использованием атрибута iloc изменяем значения в последних двух строках столбца "Result"
col_result_pos = df.columns.get_loc("Result")
df.iloc[-2:, col_result_pos] = [2340, 5270]

# d) С помощью атрибута loc изменяем значение в строке с индексом 3 в столбце "Quantity"
df.loc[3, "Quantity"] = 3

# e) С использованием атрибута iloc изменяем значение в строке с индексом 3 в столбце "Total"
col_total_pos = df.columns.get_loc("Total")
df.iloc[3, col_total_pos] = 2700

# f) С помощью атрибута loc изменяем значение в строке с индексом 3 в последнем столбце
last_column_name = df.columns[-1]
df.loc[3, last_column_name] = 2025

print("Изменённый DataFrame:")
print(df)

# Сохраняем изменённый DataFrame в новый файл
output_file = os.path.join(FOLDER_PATH, "Simple_table_modified.xlsx")
df.to_excel(output_file, index=False)  # index=False, чтобы не сохранять индексы строк
print(f"\nФайл сохранён как: {output_file}")
