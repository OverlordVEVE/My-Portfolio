import numpy as np

# Настройка формата вывода
np.set_printoptions(precision=2, suppress=True)

print("=" * 60)
print("РАЗЛИЧНЫЕ ОПЕРАЦИИ С МАССИВАМИ")
print("=" * 60)

# a) Создание двумерного массива (5, 4) со случайными целыми [0, 50)
a = np.random.randint(0, 50, size=(5, 4))
print("\na) Двумерный массив 5x4 со случайными целыми [0, 50):")
print(a)
print(f"Форма: {a.shape}, Тип: {a.dtype}")

# Суммы по строкам и столбцам
row_sums = np.sum(a, axis=1)
col_sums = np.sum(a, axis=0)

print("\nСуммы элементов по строкам (axis=1):")
print(row_sums)
print("Суммы элементов по столбцам (axis=0):")
print(col_sums)

# b) Статистические характеристики массива
mean_value = np.mean(a)
max_value = np.max(a)
min_value = np.min(a)

print("\nb) Статистические характеристики массива:")
print(f"Среднее значение элементов: {mean_value:.2f}")
print(f"Максимальное значение: {max_value}")
print(f"Минимальное значение: {min_value}")

# c) Проверка элементов на превышение 30
c_result = a > 30
print("\nc) Проверка элементов массива (a > 30):")
print("True - если элемент > 30, False - в противном случае")
print(c_result)

# d) Проверка на попадание в отрезок [12, 25]
d_result = (a >= 12) & (a <= 25)
print("\nd) Проверка элементов на попадание в отрезок [12, 25]:")
print("True - если 12 ≤ элемент ≤ 25, False - в противном случае")
print(d_result)

# e) Количество элементов меньше 18
e_count = np.sum(a < 18)
print(f"\ne) Количество элементов массива, которые меньше 18: {e_count}")

# f) Создание массива linspace и изменение формы
f = np.linspace(10, 150, 20)
print("\nf1) Одномерный массив linspace(10, 150, 20):")
print(f)
print(f"Исходная форма: {f.shape}")

f_reshaped = f.reshape(4, 5)
print("\nf2) Массив после reshape(4, 5):")
print(f_reshaped)
print(f"Новая форма: {f_reshaped.shape}")

# g) Создание двумерного массива (4, 5) со случайными целыми [0, 20)
g = np.random.randint(0, 20, size=(4, 5))
print("\ng) Двумерный массив 4x5 со случайными целыми [0, 20):")
print(g)
print(f"Форма: {g.shape}, Тип: {g.dtype}")

# h) Вертикальное соединение массивов (f_reshaped над g)
h_result = np.vstack((f_reshaped, g))
print("\nh) Вертикальное соединение массивов (np.vstack):")
print("Массив f_reshaped расположен над массивом g")
print(h_result)
print(f"Форма результата: {h_result.shape}")

# i) Горизонтальное соединение массивов (g слева, f_reshaped справа)
i_result = np.hstack((g, f_reshaped))
print("\ni) Горизонтальное соединение массивов (np.hstack):")
print("Массив g слева, массив f_reshaped справа")
print(i_result)
print(f"Форма результата: {i_result.shape}")

# j) Разделение массива f_reshaped на два объекта формы (2, 5)
j_result = np.vsplit(f_reshaped, 2)
print("\nj) Разделение массива f_reshaped на 2 объекта формы (2, 5):")
print(f"Количество частей: {len(j_result)}")
for i, part in enumerate(j_result, 1):
    print(f"\nЧасть {i}:")
    print(part)
    print(f"Форма: {part.shape}")

# k) Разделение массива f_reshaped на объекты (4, 3) и (4, 2)
k_result = np.hsplit(f_reshaped, [3])
print("\nk) Разделение массива f_reshaped на объекты (4, 3) и (4, 2):")
print(f"Количество частей: {len(k_result)}")
for i, part in enumerate(k_result, 1):
    print(f"\nЧасть {i}:")
    print(part)
    print(f"Форма: {part.shape}")

print("\n" + "=" * 60)
print("ДОПОЛНИТЕЛЬНАЯ СТАТИСТИЧЕСКАЯ ИНФОРМАЦИЯ")
print("=" * 60)

# Дополнительная статистика для массива a
print("\nМассив a - полная статистика:")
print("-" * 40)

print(f"Сумма всех элементов: {np.sum(a)}")
print(f"Среднее значение: {np.mean(a):.2f}")
print(f"Стандартное отклонение: {np.std(a):.2f}")
print(f"Дисперсия: {np.var(a):.2f}")
print(f"Медиана: {np.median(a):.2f}")
print(f"Процент элементов > 30: {np.mean(a > 30) * 100:.1f}%")
print(f"Процент элементов в [12, 25]: {np.mean((a >= 12) & (a <= 25)) * 100:.1f}%")

print("\n" + "-" * 40)
print("Сравнение массивов f_reshaped и g:")
print("-" * 40)

print("Массив f_reshaped (из linspace):")
print(f"  Форма: {f_reshaped.shape}")
print(f"  Минимум: {f_reshaped.min():.2f}")
print(f"  Максимум: {f_reshaped.max():.2f}")
print(f"  Среднее: {f_reshaped.mean():.2f}")

print("\nМассив g (случайные целые [0, 20)):")
print(f"  Форма: {g.shape}")
print(f"  Минимум: {g.min()}")
print(f"  Максимум: {g.max()}")
print(f"  Среднее: {g.mean():.2f}")

print("\n" + "=" * 60)
print("ИНФОРМАЦИЯ О РЕЗУЛЬТАТАХ ОПЕРАЦИЙ:")
print("=" * 60)

results = [
    ("a", a, "Исходный массив 5x4"),
    ("c_result", c_result, "a > 30"),
    ("d_result", d_result, "12 ≤ a ≤ 25"),
    ("f_reshaped", f_reshaped, "linspace reshaped 4x5"),
    ("g", g, "Случайный массив 4x5"),
    ("h_result", h_result, "vstack(f, g)"),
    ("i_result", i_result, "hstack(g, f)"),
]

print("\n{:15s} {:15s} {:25s} {:>10s} {:>10s}".format(
    "Имя", "Тип", "Форма", "Мин", "Макс"))
print("-" * 80)

for name, array, description in results:
    if array.dtype == bool:
        min_val = str(array.min())
        max_val = str(array.max())
    elif array.dtype in [np.float32, np.float64]:
        min_val = f"{array.min():.2f}"
        max_val = f"{array.max():.2f}"
    else:
        min_val = f"{array.min():.0f}"
        max_val = f"{array.max():.0f}"
    
    print("{:15s} {:15s} {:25s} {:>10s} {:>10s}".format(
        name, str(array.dtype), str(array.shape), min_val, max_val))

print("\n" + "=" * 60)
print("ВСЕ ОПЕРАЦИИ ВЫПОЛНЕНЫ УСПЕШНО")
print("=" * 60)
