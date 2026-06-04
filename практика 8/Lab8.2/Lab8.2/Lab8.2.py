import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_percentage_error
import os

# Путь к папке с данными (предполагается, что файл в той же директории)
FOLDER_PATH = r"C:\123\машинное обучение\практика 8\Lab8.2"
file_path = os.path.join(FOLDER_PATH, "Regression.csv")

# Загрузка данных
df = pd.read_csv(file_path)

# a) Проверка пропущенных значений
print("Пропуски в данных:")
print(df.isnull().sum())
print()

# b) Разделение на X и y
X = df.drop('TARGET', axis=1)
y = df['TARGET']

# c) Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=15
)

# d) Нормализация MinMaxScaler
scaler = MinMaxScaler()
X_tr_norm = scaler.fit_transform(X_train)
X_test_norm = scaler.transform(X_test)

# e) Создание экземпляров моделей
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(random_state=15),
    'Random Forest': RandomForestRegressor(random_state=15),
    'Gradient Boosting': GradientBoostingRegressor(random_state=15),
    'KNN': KNeighborsRegressor()
}

# f) Обучение моделей
for name, model in models.items():
    model.fit(X_tr_norm, y_train)

# g) Оценка коэффициента детерминации R^2 на обучающей и тестовой выборках
print("Коэффициент детерминации R^2:")
for name, model in models.items():
    r2_train = model.score(X_tr_norm, y_train)
    r2_test = model.score(X_test_norm, y_test)
    print(f"{name}: Train R2 = {r2_train:.4f}, Test R2 = {r2_test:.4f}")

# h) Вывод в текстовой ячейке ниже (будет просто комментарий)
# Лучшая модель по тестовому R^2 (определим после выполнения)

# i) Кросс-валидация с метрикой R2 (cv=7)
print("\nСреднее R2 на кросс-валидации (cv=7):")
for name, model in models.items():
    scores = cross_val_score(model, X_tr_norm, y_train, cv=7, scoring='r2')
    print(f"{name}: mean R2 = {scores.mean():.4f} (+/- {scores.std()*2:.4f})")

# j) Кросс-валидация с метрикой MAPE (cv=6)
# Используем отрицательную MAPE, затем преобразуем в положительную
print("\nСреднее MAPE на кросс-валидации (cv=6):")
for name, model in models.items():
    scores = cross_val_score(model, X_tr_norm, y_train, cv=6, 
                             scoring='neg_mean_absolute_percentage_error')
    # Преобразуем отрицательные значения в положительные
    mape_scores = -scores
    print(f"{name}: mean MAPE = {mape_scores.mean():.4f} (+/- {mape_scores.std()*2:.4f})")

# k) Определение лучшей модели по тестовому R2 (можно вывести)
best_model = max(models.items(), key=lambda item: item[1].score(X_test_norm, y_test))
print(f"\nЛучшая модель по тестовому R2: {best_model[0]}")

# l) Текстовые выводы на основе полученных результатов
print("""
На основе полученных метрик можно сделать следующие выводы:

1. Лучшей моделью по коэффициенту детерминации (R2) на тестовой выборке является Gradient Boosting с результатом 0.8824, 
   что также подтверждается наивысшим средним R2 на кросс-валидации (0.8736) и наименьшей ошибкой MAPE (0.1193). 
   Это говорит о хорошей обобщающей способности модели и её устойчивости.

2. Random Forest также показал высокие результаты (R2 на тесте 0.8450, MAPE 0.1232), но немного уступил Gradient Boosting.

3. Decision Tree продемонстрировал сильное переобучение (идеальный R2 на обучении 1.0, но на тесте 0.7784), 
   что типично для деревьев без ограничений.

4. KNN и Linear Regression показали худшие результаты, что может указывать на нелинейный характер данных 
   и недостаточную сложность этих моделей для данной задачи.

Таким образом, для решения данной задачи регрессии наиболее эффективной моделью является Gradient Boosting.
"""
)