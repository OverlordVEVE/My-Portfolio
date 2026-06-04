import pandas as pd
import os

# Путь к папке с данными
FOLDER_PATH = r"C:\123\машинное обучение\практика 5\Lab5.4"
INPUT_FILE = os.path.join(FOLDER_PATH, "Birds.xlsx")

# Загружаем данные
df = pd.read_excel(INPUT_FILE)

# Пункт b: группировка по Name, средние значения Max Speed и Weight
grouped_b = df.groupby('Name')[['Max Speed', 'Weight']].mean()
output_b = os.path.join(FOLDER_PATH, "Birds_b.xlsx")
grouped_b.to_excel(output_b)
print(f"Сохранён файл {output_b}")

# Пункт c: группировка по Family, максимумы и средние для обоих столбцов
grouped_c = df.groupby('Family').agg({
    'Max Speed': ['max', 'mean'],
    'Weight': ['max', 'mean']
})
output_c = os.path.join(FOLDER_PATH, "Birds_c.xlsx")
grouped_c.to_excel(output_c)
print(f"Сохранён файл {output_c}")

# Пункт d: группировка по Family, для Max Speed – среднее, для Weight – min и max
grouped_d = df.groupby('Family').agg({
    'Max Speed': 'mean',
    'Weight': ['min', 'max']
})
output_d = os.path.join(FOLDER_PATH, "Birds_d.xlsx")
grouped_d.to_excel(output_d)
print(f"Сохранён файл {output_d}")

# Пункт e: группировка по Family и Name, для Max Speed – max, для Weight – min
grouped_e = df.groupby(['Family', 'Name']).agg({
    'Max Speed': 'max',
    'Weight': 'min'
})
output_e = os.path.join(FOLDER_PATH, "Birds_e.xlsx")
grouped_e.to_excel(output_e)
print(f"Сохранён файл {output_e}")
