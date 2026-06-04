import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Исходные данные
X_list = [10, 12, 15, 20, 25, 30, 34, 40, 47, 54, 57]
y_list = [80, 75, 70, 63, 65, 70, 76, 85, 90, 92, 87]

X = np.array(X_list)
y = np.array(y_list)

# а) Преобразуем X в матрицу-столбец
X_ = X.reshape(-1, 1)

# б) Создаем объект PolynomialFeatures степени 5
poly = PolynomialFeatures(degree=5)

# в) Преобразуем X_ в полиномиальные признаки
X_poly = poly.fit_transform(X_)

# г) Создаем объект линейной регрессии
reg = LinearRegression()

# д) Обучаем модель на полиномиальных признаках
reg.fit(X_poly, y)

# е) Создаем тестовый набор значений X от 5 до 64
X_test = np.arange(5, 65).reshape(-1, 1)

# ж) Преобразуем тестовые данные в полиномиальные признаки
X_test_poly = poly.fit_transform(X_test)  # согласно заданию используем fit_transform

# з) Получаем предсказания модели
y_test = reg.predict(X_test_poly)

# и) Строим график
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='red', label='Исходные данные')
plt.plot(X_test, y_test, color='blue', label='Полиномиальная регрессия (степень 5)')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Полиномиальная регрессия')
plt.legend()
plt.grid(True)
plt.show()
