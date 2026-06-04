import pandas as pd
import matplotlib.pyplot as plt
import os

# Путь к файлу
FOLDER_PATH = r"C:\123\машинное обучение\практика 7\Lab7.5"
file_path = os.path.join(FOLDER_PATH, "iris.csv")

# Загрузка данных
df = pd.read_csv(file_path)

# а) Гистограмма для sepal.length
plt.figure(figsize=(8, 5))
plt.hist(df['sepal.length'], bins=20, edgecolor='k', alpha=0.7)
plt.title('Гистограмма длины чашелистика (sepal.length)')
plt.xlabel('Длина чашелистика (см)')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.3)
plt.show()

# б) Гистограмма для petal.length с оформлением
plt.figure(figsize=(8, 5))
plt.hist(df['petal.length'], bins=15, color='orange', edgecolor='red', linewidth=1.5, alpha=0.6)
plt.title('Гистограмма длины лепестка (petal.length)', fontsize=14)
plt.xlabel('Длина лепестка (см)', fontsize=12)
plt.ylabel('Количество', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# в) Диаграмма размаха для petal.width
plt.figure(figsize=(6, 4))
plt.boxplot(df['petal.width'], vert=True, patch_artist=True,
            boxprops=dict(facecolor='lightblue'))
plt.title('Диаграмма размаха ширины лепестка (petal.width)')
plt.ylabel('Ширина лепестка (см)')
plt.grid(axis='y', alpha=0.3)
plt.show()

# г) Диаграммы размаха для sepal.width и petal.width на одном графике
plt.figure(figsize=(8, 6))
data_to_plot = [df['sepal.width'], df['petal.width']]
plt.boxplot(data_to_plot, labels=['sepal.width', 'petal.width'],
            patch_artist=True,
            boxprops=dict(facecolor='lightgreen'),
            medianprops=dict(color='red', linewidth=2),
            whiskerprops=dict(color='blue'),
            capprops=dict(color='blue'),
            flierprops=dict(marker='o', markerfacecolor='gray', markersize=5))
plt.title('Сравнение ширины чашелистика и лепестка', fontsize=14)
plt.ylabel('Ширина (см)', fontsize=12)
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()
