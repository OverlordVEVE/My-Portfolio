# -*- coding: utf-8 -*-
"""
Решение задачи классификации (практика 9, Lab9.1)
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report

# Путь к папке с данными
FOLDER_PATH = r"C:\123\машинное обучение\практика 9\Lab9.1"

# а) Загрузка данных
df = pd.read_csv(FOLDER_PATH + r"\Classification.csv")  # предполагаем расширение .csv
X = df.drop('TARGET', axis=1)
y = df['TARGET']

# б) Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.25, random_state=15
)

# в) Импорт классов классификаторов (5 шт.)
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Создание экземпляров с параметрами по умолчанию
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),  # увеличим max_iter для сходимости
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC(),
    'k-NN': KNeighborsClassifier()
}

# г) Обучение моделей и д) оценка accuracy на train и test
print("Accuracy на обучающем и тестовом наборах:\n")
for name, model in models.items():
    model.fit(X_train, y_train)
    train_acc = model.score(X_train, y_train)
    test_acc = model.score(X_test, y_test)
    print(f"{name:20} Train: {train_acc:.4f}, Test: {test_acc:.4f}")

#Лучший результат на тестовой выборке показала модель Random Forest с точностью 0.7733.  
#Она также лидирует по усреднённой точности при кросс-валидации (0.7822). 
#Ближе всех к ней подобрался SVM (0.7644 на тесте и 0.7533 на кросс-валидации),  однако Random Forest всё же превосходит его по обоим показателям")

# ж) Отчет classification_report для каждой модели на тестовых данных
print("\n" + "="*60)
print("Classification Report на тестовых данных:\n")
for name, model in models.items():
    y_pred = model.predict(X_test)
    print(f"--- {name} ---")
    print(classification_report(y_test, y_pred))

# з) Кросс-валидация с cv=4
print("="*60)
print("Средняя accuracy при кросс-валидации (cv=4):\n")
for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=4, scoring='accuracy')
    print(f"{name:20} Mean accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")

# и)
#Переобучение
#Модели Decision Tree и Random Forest показали 100% точность на обучающей выборке, что указывает на склонность к переобучению.
#Однако Random Forest благодаря ансамблированию лучше обобщает: его точность на тесте (0.7733) значительно выше, чем у одиночного дерева (0.6933).
#Сравнение моделей
#Logistic Regression оказалась самой слабой (0.6578 на тесте). Вероятно, данные не являются линейно разделимыми.
#k-NN (0.7111) и Decision Tree (0.6933) показали средние результаты, уступая более сложным алгоритмам.
#SVM с линейным ядром (по умолчанию) дал хороший результат (0.7644), но всё же немного хуже Random Forest.
#Random Forest – безусловный лидер как по accuracy на тесте, так и по усреднённой кросс-валидации.
#Анализ по классам (classification report)
#У всех моделей наблюдаются трудности с классом 2 – для него значения recall и f1-score заметно ниже, чем для классов 0 и 1.
#Random Forest и SVM лучше остальных справляются с этим классом, демонстрируя более сбалансированные метрики.
#Дисбаланс классов отсутствует (подвыборки примерно равны), поэтому проблема связана со сложностью разделения именно этого класса в пространстве признаков.
#Стабильность моделей (кросс-валидация)
#Наименьший разброс точности при кросс-валидации у Logistic Regression (±0.0205) и k-NN (±0.0179), но их средняя точность невысока.
#Random Forest имеет наибольший разброс (±0.0476), что говорит о некоторой чувствительности к разбиению данных, однако его средняя точность всё равно остаётся самой высокой.