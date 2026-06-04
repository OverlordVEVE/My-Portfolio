import numpy as np

# Настройка формата вывода
np.set_printoptions(precision=2, suppress=True)

print("=" * 60)
print("ДОПОЛНИТЕЛЬНЫЕ ФУНКЦИИ NUMPY")
print("=" * 60)

# a) Создание двумерного массива (5, 4) со случайными значениями [-5, 10)
print("\na) Создание двумерного массива 5x4 со случайными значениями [-5, 10):")
a = np.random.uniform(-5, 10, size=(5, 4))
print("Исходный массив a:")
print(a)
print(f"Форма: {a.shape}, Тип: {a.dtype}")

# Вычисление суммы элементов на главной диагонали
# Для неквадратной матрицы главная диагональ имеет длину min(rows, cols)
diag_sum = np.trace(a)
print(f"\nСумма элементов на главной диагонали (np.trace): {diag_sum:.2f}")

# Альтернативный способ
diag_elements = np.diag(a)
print("Элементы на главной диагонали:", diag_elements)
print(f"Подтверждение суммы: {np.sum(diag_elements):.2f}")

# b) Создание массива со значениями "Pos", "Neg", "Zero" с помощью select
print("\n\nb) Создание массива со значениями 'Pos', 'Neg', 'Zero' (np.select):")

# Определяем условия
conditions = [
    a > 0,   # Условие 1: элементы больше 0
    a < 0    # Условие 2: элементы меньше 0
]

# Определяем значения для каждого условия
choices = [
    "Pos",   # Значение для условия 1
    "Neg"    # Значение для условия 2
]

# Создаем массив с помощью select
b = np.select(conditions, choices, default="Zero")
print("Массив b (Pos/Neg/Zero):")
print(b)
print(f"Форма: {b.shape}, Тип: {b.dtype}")

# Подсчет количества элементов каждой категории
pos_count = np.sum(b == "Pos")
neg_count = np.sum(b == "Neg")
zero_count = np.sum(b == "Zero")
print(f"\nКоличество элементов:")
print(f"  Pos (положительные): {pos_count}")
print(f"  Neg (отрицательные): {neg_count}")
print(f"  Zero (нулевые): {zero_count}")

# c) Создание булева массива: True для "Zero" и "Neg", False для "Pos"
print("\n\nc) Создание булева массива (True для 'Zero' и 'Neg', False для 'Pos'):")
c = (b == "Zero") | (b == "Neg")
print("Булев массив c:")
print(c)
print(f"Форма: {c.shape}, Тип: {c.dtype}")

# Проверка
print(f"\nПроверка:")
print(f"  Количество True (Zero или Neg): {np.sum(c)}")
print(f"  Количество False (Pos): {np.sum(~c)}")

# Сравнение с исходными данными
print("\nСравнение с исходным массивом a:")
print("Первые 3x3 элемента для сравнения:")
print("a:")
print(a[:3, :3])
print("\nb (категории):")
print(b[:3, :3])
print("\nc (булев):")
print(c[:3, :3])

# d) Получение индексов для сортировки по вертикали
print("\n\nd) Получение индексов для сортировки элементов по столбцам:")

# Получаем индексы, которые отсортируют каждый столбец от меньшего к большему
d_argsort = np.argsort(a, axis=0)
print("Индексы для сортировки каждого столбца (axis=0):")
print(d_argsort)
print(f"Форма: {d_argsort.shape}, Тип: {d_argsort.dtype}")

# Проверка: применяем индексы для сортировки
print("\nПроверка сортировки:")
for col in range(a.shape[1]):
    print(f"\nСтолбец {col}:")
    print(f"  Исходный: {a[:, col]}")
    sorted_col = a[d_argsort[:, col], col]
    print(f"  Отсортированный: {sorted_col}")
    print(f"  Индексы для сортировки: {d_argsort[:, col]}")

# Создаем отсортированный массив
a_sorted_by_cols = np.take_along_axis(a, d_argsort, axis=0)
print("\nМассив a, отсортированный по столбцам:")
print(a_sorted_by_cols)

# e) Получение индексов элементов, больших 3
print("\n\ne) Получение индексов элементов, больших 3 (np.where):")

# Используем np.where для получения индексов
e_indices = np.where(a > 3)
print(f"Индексы элементов, больших 3:")
print(f"  Индексы строк: {e_indices[0]}")
print(f"  Индексы столбцов: {e_indices[1]}")

# Количество элементов, больших 3
num_greater_than_3 = len(e_indices[0])
print(f"Количество элементов > 3: {num_greater_than_3}")

# Выводим пары индексов и значения
print("\nЭлементы, большие 3 (строка, столбец, значение):")
for i in range(min(10, num_greater_than_3)):  # Показываем первые 10 элементов
    row, col = e_indices[0][i], e_indices[1][i]
    value = a[row, col]
    print(f"  ({row}, {col}): {value:.2f}")

# Альтернативный формат вывода
print("\nМассив с координатами элементов > 3:")
coordinates = np.column_stack(e_indices)
print(coordinates)

print("\n" + "=" * 60)
print("ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ И ПРОВЕРКА")
print("=" * 60)

# Дополнительный анализ массива a
print("\n1. Статистика массива a:")
print("-" * 40)
print(f"Минимум: {np.min(a):.2f}")
print(f"Максимум: {np.max(a):.2f}")
print(f"Среднее: {np.mean(a):.2f}")
print(f"Медиана: {np.median(a):.2f}")
print(f"Стандартное отклонение: {np.std(a):.2f}")

print("\n2. Анализ главной диагонали:")
print("-" * 40)
print(f"Элементы на главной диагонали: {diag_elements}")
print(f"Минимум на диагонали: {np.min(diag_elements):.2f}")
print(f"Максимум на диагонали: {np.max(diag_elements):.2f}")
print(f"Среднее на диагонали: {np.mean(diag_elements):.2f}")

print("\n3. Сравнение различных представлений массива:")
print("-" * 40)
print("Первые 2 строки для сравнения:")
print("\nМассив a (числовой):")
print(a[:2])
print("\nМассив b (категории):")
print(b[:2])
print("\nМассив c (булев, True=Zero/Neg):")
print(c[:2])

print("\n4. Проверка сортировки по столбцам:")
print("-" * 40)
for col in range(min(3, a.shape[1])):  # Проверяем первые 3 столбца
    print(f"\nСтолбец {col}:")
    print(f"  Исходные значения: {a[:, col]}")
    print(f"  Индексы сортировки: {d_argsort[:, col]}")
    print(f"  Отсортированные значения: {a_sorted_by_cols[:, col]}")
    
    # Проверяем, что значения действительно отсортированы
    is_sorted = np.all(a_sorted_by_cols[1:, col] >= a_sorted_by_cols[:-1, col])
    print(f"  Проверка сортировки (по возрастанию): {'Пройдена' if is_sorted else 'Не пройдена'}")

print("\n5. Подробная информация об элементах > 3:")
print("-" * 40)
if num_greater_than_3 > 0:
    # Группируем по строкам
    print("Элементы > 3, сгруппированные по строкам:")
    for row in range(a.shape[0]):
        row_indices = np.where(e_indices[0] == row)[0]
        if len(row_indices) > 0:
            print(f"  Строка {row}: ", end="")
            elements = []
            for idx in row_indices:
                col = e_indices[1][idx]
                value = a[row, col]
                elements.append(f"col{col}={value:.2f}")
            print(", ".join(elements))
    
    # Статистика по элементам > 3
    values_greater_than_3 = a[e_indices]
    print(f"\nСтатистика по элементам > 3:")
    print(f"  Минимальное значение > 3: {np.min(values_greater_than_3):.2f}")
    print(f"  Максимальное значение > 3: {np.max(values_greater_than_3):.2f}")
    print(f"  Среднее значение > 3: {np.mean(values_greater_than_3):.2f}")
    print(f"  Сумма всех значений > 3: {np.sum(values_greater_than_3):.2f}")
else:
    print("  Нет элементов, больших 3")

print("\n" + "=" * 60)
print("СВОДНАЯ ИНФОРМАЦИЯ О ВСЕХ МАССИВАХ")
print("=" * 60)

arrays = [
    ("a", a, "Исходный числовой массив"),
    ("b", b, "Категории Pos/Neg/Zero"),
    ("c", c, "Булев массив (True=Zero/Neg)"),
    ("d_argsort", d_argsort, "Индексы для сортировки по столбцам"),
    ("a_sorted_by_cols", a_sorted_by_cols, "Отсортированный по столбцам")
]

print("\n{:15s} {:20s} {:15s} {:>10s} {:>10s}".format(
    "Имя", "Форма", "Тип", "Мин", "Макс"))
print("-" * 80)

for name, array, description in arrays:
    if array.dtype == bool:
        min_val = str(array.min())
        max_val = str(array.max())
    elif array.dtype.kind in 'SU':  # Строковый тип
        min_val = "-"
        max_val = "-"
    elif array.dtype.kind in 'iufc':  # Числовые типы
        min_val = f"{array.min():.2f}"
        max_val = f"{array.max():.2f}"
    else:
        min_val = f"{array.min()}"
        max_val = f"{array.max()}"
    
    print("{:15s} {:20s} {:15s} {:>10s} {:>10s}".format(
        name, str(array.shape), str(array.dtype), min_val, max_val))

print("\n" + "=" * 60)
print("ВСЕ ОПЕРАЦИИ ВЫПОЛНЕНЫ УСПЕШНО")
print("=" * 60)
