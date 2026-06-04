import pandas as pd
import matplotlib.pyplot as plt
import os

# Путь к файлу
FOLDER_PATH = r"C:\123\машинное обучение\практика 7\Lab7.3"
file_path = os.path.join(FOLDER_PATH, "Birds.xlsx")

# Загрузка данных
df = pd.read_excel(file_path)

# а) Группировка по семейству и вычисление средней максимальной скорости
grouped = df.groupby('Family', as_index=False)['Max Speed'].mean()

# б) Извлечение значений в переменные x и y
x = grouped['Family'].values
y = grouped['Max Speed'].values

# в) Простая столбчатая диаграмма (вертикальная)
plt.figure()
plt.bar(x, y)
plt.title('в) Вертикальная столбчатая диаграмма (без оформления)')
plt.show()

# г) Простая горизонтальная столбчатая диаграмма
plt.figure()
plt.barh(x, y)
plt.title('г) Горизонтальная столбчатая диаграмма (без оформления)')
plt.show()

# д) Оформленные диаграммы

# Вертикальная с оформлением
plt.figure(figsize=(10, 6))
plt.bar(x, y, color='skyblue', edgecolor='black')
plt.title('Средняя максимальная скорость по семействам птиц', fontsize=14)
plt.xlabel('Семейство', fontsize=12)
plt.ylabel('Средняя максимальная скорость (км/ч)', fontsize=12)
plt.xticks(rotation=45, ha='right')  # поворот подписей для читаемости
plt.tight_layout()
plt.show()

# Горизонтальная с оформлением
plt.figure(figsize=(10, 8))
plt.barh(x, y, color='lightcoral', edgecolor='black')
plt.title('Средняя максимальная скорость по семействам птиц', fontsize=14)
plt.xlabel('Средняя максимальная скорость (км/ч)', fontsize=12)
plt.ylabel('Семейство', fontsize=12)
plt.tight_layout()
plt.show()
