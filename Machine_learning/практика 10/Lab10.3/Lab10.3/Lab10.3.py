# Алгоритм DBSCAN

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

# Путь к данным
FOLDER_PATH = r"C:\123\машинное обучение\практика 10\Lab10.3"

# а) Загрузка данных
df = pd.read_csv(FOLDER_PATH + r"\Task3.csv")  # файл Task3.csv

# б) Создание и обучение DBSCAN
dbscan = DBSCAN(eps=0.45, min_samples=12)
dbscan.fit(df)

# в) Получение меток кластеров
labels = dbscan.labels_

# г) PCA для визуализации
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df)

# д) Создание DataFrame с результатами PCA и метками
res = pd.DataFrame(df_pca, columns=['PC1', 'PC2'])
res['cluster'] = labels

# е) Построение диаграммы рассеяния
plt.figure(figsize=(8, 6))
sns.scatterplot(data=res, x='PC1', y='PC2', hue='cluster', palette='Set2', s=70)
plt.title('DBSCAN кластеризация (PCA проекция)')
plt.xlabel('Первая главная компонента')
plt.ylabel('Вторая главная компонента')
plt.legend(title='Кластер')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Вывод количества кластеров (исключая шум, если есть)
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
print(f"Количество кластеров, выделенных DBSCAN (без учёта шума): {n_clusters}")
print(f"Количество шумовых точек (метка -1): {list(labels).count(-1)}")
