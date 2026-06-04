import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Путь к папке с данными
FOLDER_PATH = r"C:\123\машинное обучение\практика 7\Lab7.6"
file_path = FOLDER_PATH + "\\iris.csv"  # или os.path.join

# Загрузка данных
df = pd.read_csv(file_path)

# а) 3D диаграмма рассеяния с цветом по petal.width
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(df['petal.length'], df['sepal.length'], df['sepal.width'],
                c=df['petal.width'], cmap='viridis', s=30)
ax.set_xlabel('Petal Length')
ax.set_ylabel('Sepal Length')
ax.set_zlabel('Sepal Width')
plt.colorbar(sc, label='Petal Width')
plt.title('3D Scatter: Iris dataset')
plt.show()

# б) Каркасная поверхность (plot_wireframe) для произвольной функции
# Создадим данные для функции f(x,y) = x * exp(-x^2 - y^2)
x = np.linspace(-2, 2, 30)
y = np.linspace(-2, 2, 30)
X, Y = np.meshgrid(x, y)
Z = X * np.exp(-X**2 - Y**2)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, color='blue', linewidth=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Wireframe: f(x,y) = x * exp(-x^2 - y^2)')
plt.show()

# в) Поверхность (plot_surface) для другой функции: f(x,y) = sin(x) * cos(y)
x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none', alpha=0.8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.colorbar(surf, label='sin(X)*cos(Y)')
plt.title('Surface: f(x,y) = sin(X) * cos(Y)')
plt.show()

# г) Контурные графики (contour и contourf) на одном рисунке в двух подграфиках
# Используем ту же функцию, что и в пункте в (или другую)
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# левый подграфик: contourf (заполненный)
contourf = ax1.contourf(X, Y, Z, levels=20, cmap='coolwarm')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('Contourf: заполненный')
fig.colorbar(contourf, ax=ax1)

# правый подграфик: contour (линии)
contour = ax2.contour(X, Y, Z, levels=20, cmap='coolwarm')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('Contour: линии')
fig.colorbar(contour, ax=ax2)

plt.suptitle('Контурные графики функции sin(X)*cos(Y)')
plt.show()
