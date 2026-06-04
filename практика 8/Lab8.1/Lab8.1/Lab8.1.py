import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os

# Путь к папке с данными
FOLDER_PATH = r"C:\123\машинное обучение\практика 8\Lab8.1"
file_path = os.path.join(FOLDER_PATH, "LinReg1.csv")

# Загрузка данных
df = pd.read_csv(file_path)

# a) Проверка пропущенных значений
print("Информация о данных:")
df.info()
print("\nКоличество пропусков по столбцам:")
print(df.isna().sum())

# b) Тепловая карта корреляций с помощью matplotlib
plt.figure(figsize=(8, 6))
corr_matrix = df.corr()
# Используем imshow для отображения матрицы корреляции
plt.imshow(corr_matrix, cmap='coolwarm', interpolation='nearest', aspect='auto')
plt.colorbar(label='Корреляция')
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45, ha='right')
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.title('Тепловая карта корреляций')
# Добавляем значения в ячейки
for i in range(len(corr_matrix.columns)):
    for j in range(len(corr_matrix.columns)):
        plt.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}', ha='center', va='center', color='white' if abs(corr_matrix.iloc[i, j]) > 0.5 else 'black')
plt.tight_layout()
plt.show()

# c) Разделение на X и y
X = df.drop('height_target', axis=1)
y = df['height_target']

# d) Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=15
)

# e) Создание модели линейной регрессии
lin_reg = LinearRegression()

# f) Обучение модели
lin_reg.fit(X_train, y_train)

# g) Оценка коэффициента детерминации (R^2)
r2_train = lin_reg.score(X_train, y_train)
r2_test = lin_reg.score(X_test, y_test)
print(f"R^2 на обучающей выборке: {r2_train:.4f}")
print(f"R^2 на тестовой выборке: {r2_test:.4f}")

# h) Получение коэффициентов регрессии
print(f"Свободный член (intercept): {lin_reg.intercept_}")
print("Коэффициенты при признаках:")
for feature, coef in zip(X.columns, lin_reg.coef_):
    print(f"  {feature}: {coef:.4f}")
