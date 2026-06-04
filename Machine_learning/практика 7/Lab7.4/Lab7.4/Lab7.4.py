import pandas as pd
import matplotlib.pyplot as plt
import os

# Путь к папке с данными
FOLDER_PATH = r"C:\123\машинное обучение\практика 7\Lab7.4"
file_path = os.path.join(FOLDER_PATH, "Birds.xlsx")

# Загрузка данных
df = pd.read_excel(file_path)

# а) Группировка по семейству и вычисление средней максимальной скорости
grouped = df.groupby('Family', as_index=False)['Max Speed'].mean()

# Извлечение значений в переменные x (метки) и y (числовые значения)
x = grouped['Family'].values
y = grouped['Max Speed'].values

# б) Простая круговая диаграмма
plt.figure(figsize=(8, 8))
plt.pie(y, labels=x)
plt.title('б) Круговая диаграмма (без оформления)')
plt.show()

# в) Оформленная круговая диаграмма с дополнительными параметрами
# Создадим эффект "вырывания" первого сектора
explode = [0.1 if i == 0 else 0 for i in range(len(x))]

plt.figure(figsize=(10, 8))
plt.pie(y,
        labels=x,
        autopct='%1.1f%%',      # отображение процентов с одним знаком после запятой
        shadow=True,             # тень
        explode=explode,         # выделение первого сектора
        startangle=90,           # начальный угол поворота
        counterclock=False)      # по часовой стрелке
plt.title('в) Средняя максимальная скорость по семействам птиц (оформленная)', fontsize=14)
plt.axis('equal')                # чтобы круг был круглым
plt.tight_layout()
plt.show()
