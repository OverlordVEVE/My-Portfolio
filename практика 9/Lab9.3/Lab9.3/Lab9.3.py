

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Путь к папке с данными
FOLDER_PATH = r"C:\123\машинное обучение\практика 9\Lab9.3"

# а) Загрузка данных
df = pd.read_csv(FOLDER_PATH + r"\Wine_cls.csv")  # предполагаем расширение .csv
X = df.drop('class', axis=1)
y = df['class']

# б) Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.25, random_state=15
)

# в) Создание экземпляров ансамблевых методов с параметрами по усмотрению

# 1. BaggingClassifier (на основе дерева решений)
bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=50,
    random_state=15
)

# 2. AdaBoostClassifier (на основе дерева решений)
adaboost = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=1),  # слабый классификатор (пень)
    n_estimators=50,
    random_state=15
)

# 3. StackingClassifier
# Определяем базовые модели
base_models = [
    ('lr', LogisticRegression(max_iter=1000)),
    ('dt', DecisionTreeClassifier(max_depth=5)),
    ('svm', SVC(kernel='rbf', probability=True))  # probability=True для работы с predict_proba
]
# Мета-классификатор
meta_model = LogisticRegression()
stacking = StackingClassifier(
    estimators=base_models,
    final_estimator=meta_model,
    cv=5  # внутренняя кросс-валидация для stacking
)

# Обучение моделей
bagging.fit(X_train, y_train)
adaboost.fit(X_train, y_train)
stacking.fit(X_train, y_train)

# г) Оценка accuracy на обучающем и тестовом множествах
print("Accuracy на обучающем и тестовом наборах:\n")
models = {
    'Bagging': bagging,
    'AdaBoost': adaboost,
    'Stacking': stacking
}
for name, model in models.items():
    train_acc = model.score(X_train, y_train)
    test_acc = model.score(X_test, y_test)
    print(f"{name:10} Train: {train_acc:.4f}, Test: {test_acc:.4f}")

# д) Кросс-валидация (cv=4)
print("\n" + "="*60)
print("Средняя accuracy при кросс-валидации (cv=4):\n")
for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=4, scoring='accuracy')
    print(f"{name:10} Mean accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")

# е) Текстовый вывод 
# На тестовой выборке лучший результат показали AdaBoost и Stacking (точность 0.9778), немного опередив Bagging (0.9556). 
# Однако при кросс-валидации Stacking оказался наиболее стабильным и точным (0.9609), тогда как AdaBoost продемонстрировал заметно более низкую среднюю точность (0.9164) 
# и больший разброс, что указывает на возможную чувствительность к разбиению данных. 
# Bagging показал хорошие, но чуть более слабые результаты (тест 0.9556, CV 0.9443). 
# Таким образом, наилучшей моделью для данного набора данных является StackingClassifier, 
# который благодаря комбинации различных базовых алгоритмов и мета-уровня обеспечивает высокое качество и устойчивость.
