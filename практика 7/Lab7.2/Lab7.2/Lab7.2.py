import pandas as pd
import matplotlib.pyplot as plt
import os

# Путь к папке с данными
FOLDER_PATH = r"C:\123\машинное обучение\практика 7\Lab7.2"
file_path = os.path.join(FOLDER_PATH, "iris.csv")

# Загрузка данных
df = pd.read_csv(file_path)

# Извлечение столбцов sepal.length и sepal.width
x = df['sepal.length']
y = df['sepal.width']

# Создание фигуры с четырьмя подграфиками (2x2)
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# а) Диаграмма рассеяния с параметрами по умолчанию
axs[0, 0].scatter(x, y)
axs[0, 0].set_title('а) Базовый scatter')
axs[0, 0].set_xlabel('sepal.length')
axs[0, 0].set_ylabel('sepal.width')

# б) Диаграмма с размером точек 15
axs[0, 1].scatter(x, y, s=15)
axs[0, 1].set_title('б) Размер точек = 15')
axs[0, 1].set_xlabel('sepal.length')
axs[0, 1].set_ylabel('sepal.width')

# в) Диаграмма с изменённым маркером и цветом
axs[1, 0].scatter(x, y, marker='^', color='green')
axs[1, 0].set_title('в) Маркер "^", цвет зелёный')
axs[1, 0].set_xlabel('sepal.length')
axs[1, 0].set_ylabel('sepal.width')

# г) Диаграмма с заданными linewidths и edgecolors
axs[1, 1].scatter(x, y, linewidths=1, edgecolors='red')
axs[1, 1].set_title('г) linewidths=1, edgecolors=red')
axs[1, 1].set_xlabel('sepal.length')
axs[1, 1].set_ylabel('sepal.width')

# Автоматическое выравнивание подграфиков
plt.tight_layout()
plt.show()
