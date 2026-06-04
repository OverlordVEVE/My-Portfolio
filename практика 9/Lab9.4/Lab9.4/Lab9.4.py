

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Путь к папке с данными (при необходимости измените)
FOLDER_PATH = r"C:\123\машинное обучение\практика 9\Lab9.4"

# а) Загрузка данных
df = pd.read_csv(FOLDER_PATH + r"\Wine_cls.csv")
X = df.drop('class', axis=1)
y = df['class']

# б) Стандартизация признаков
scaler = StandardScaler()
X_sc = scaler.fit_transform(X)

# в) PCA с двумя компонентами
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_sc)

# г) Создание DataFrame с результатами PCA и добавление столбца с классами
res = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
res['class'] = y.values  # добавляем целевую переменную

# д) Построение диаграммы рассеяния
plt.figure(figsize=(8, 6))
sns.scatterplot(data=res, x='PC1', y='PC2', hue='class', palette='Set2', s=70)
plt.title('PCA проекция данных Wine (2 компоненты)')
plt.xlabel('Первая главная компонента')
plt.ylabel('Вторая главная компонента')
plt.legend(title='Класс')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Дополнительно можно вывести объяснённую долю дисперсии
print(f"Объяснённая доля дисперсии: PC1 = {pca.explained_variance_ratio_[0]:.3f}, PC2 = {pca.explained_variance_ratio_[1]:.3f}")
print(f"Суммарная объяснённая дисперсия: {pca.explained_variance_ratio_.sum():.3f}")
