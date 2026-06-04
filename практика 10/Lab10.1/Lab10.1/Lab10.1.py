import pandas as pd
from sklearn.cluster import AgglomerativeClustering, KMeans

# Путь к данным
FOLDER_PATH = r"C:\123\машинное обучение\практика 10\Lab10.1"

# а) Загрузка данных
df = pd.read_csv(FOLDER_PATH + r"\Wine_cls.csv")
X = df.drop('class', axis=1)
y = df['class']

# б) Создание и обучение моделей кластеризации
aggl = AgglomerativeClustering(n_clusters=3)
kmeans = KMeans(n_clusters=3, random_state=15)

aggl.fit(X)
kmeans.fit(X)

# в) Копия данных и добавление меток кластеров
res = df.copy()
res['cluster_aggl'] = aggl.labels_
res['cluster_kmeans'] = kmeans.labels_

# г) Частота встречаемости кластеров
print("Частоты кластеров (AgglomerativeClustering):")
print(res['cluster_aggl'].value_counts().sort_index())
print("\nЧастоты кластеров (KMeans):")
print(res['cluster_kmeans'].value_counts().sort_index())

# д) Получение значений для сравнения
true_labels = y.values
aggl_labels = res['cluster_aggl'].values
kmeans_labels = res['cluster_kmeans'].values

# Таблицы сопряжённости
print("\nСравнение истинных классов с кластерами Agglomerative:")
print(pd.crosstab(true_labels, aggl_labels, rownames=['Истинный класс'], colnames=['Кластер Aggl']))
print("\nСравнение истинных классов с кластерами KMeans:")
print(pd.crosstab(true_labels, kmeans_labels, rownames=['Истинный класс'], colnames=['Кластер KMeans']))


#Общий вывод: 
#AgglomerativeClustering показал значительно лучшее соответствие истинным классам, выделив три кластера, 
#каждый из которых соответствует преимущественно одному сорту (пусть и с некоторым смешением класса 2 с классом 1). 
#KMeans же продемонстрировал неудовлетворительный результат, объединив два класса в один и разбив третий. 
#Вероятно, это связано с чувствительностью KMeans к масштабу признаков и форме кластеров; 
#при отсутствии стандартизации данных и возможной нелинейной структуре KMeans не смог корректно разделить классы. 
#Для повышения качества кластеризации рекомендуется предварительно стандартизировать признаки и, возможно, использовать другие методы или настраивать параметры.




# Задание 2: Метрики качества кластеризации

from sklearn.metrics import homogeneity_score
from sklearn.metrics import homogeneity_completeness_v_measure
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import silhouette_score

# Используем данные и метки из предыдущего задания
# X, y, aggl, kmeans уже определены

# а) Homogeneity score
hom_aggl = homogeneity_score(y, aggl.labels_)
hom_kmeans = homogeneity_score(y, kmeans.labels_)
print("Homogeneity score:")
print(f"AgglomerativeClustering: {hom_aggl:.4f}")
print(f"KMeans: {hom_kmeans:.4f}\n")

# б) Homogeneity, completeness, V-measure
hcv_aggl = homogeneity_completeness_v_measure(y, aggl.labels_)
hcv_kmeans = homogeneity_completeness_v_measure(y, kmeans.labels_)
print("Homogeneity, Completeness, V-measure (Agglomerative):")
print(f"  Homogeneity: {hcv_aggl[0]:.4f}, Completeness: {hcv_aggl[1]:.4f}, V-measure: {hcv_aggl[2]:.4f}")
print("Homogeneity, Completeness, V-measure (KMeans):")
print(f"  Homogeneity: {hcv_kmeans[0]:.4f}, Completeness: {hcv_kmeans[1]:.4f}, V-measure: {hcv_kmeans[2]:.4f}\n")

# в) Davies-Bouldin index (чем меньше, тем лучше)
db_aggl = davies_bouldin_score(X, aggl.labels_)
db_kmeans = davies_bouldin_score(X, kmeans.labels_)
print("Davies-Bouldin score (ниже = лучше):")
print(f"AgglomerativeClustering: {db_aggl:.4f}")
print(f"KMeans: {db_kmeans:.4f}\n")

# г) Silhouette score (от -1 до 1, чем ближе к 1, тем лучше)
sil_aggl = silhouette_score(X, aggl.labels_)
sil_kmeans = silhouette_score(X, kmeans.labels_)
print("Silhouette score:")
print(f"AgglomerativeClustering: {sil_aggl:.4f}")
print(f"KMeans: {sil_kmeans:.4f}")