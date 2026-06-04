import numpy as np

# Настройка формата вывода
np.set_printoptions(precision=2, suppress=True)

print("=" * 60)
print("NUMPY. РАЗЛИЧНЫЕ ФУНКЦИИ ПО ИЗМЕНЕНИЮ МАССИВОВ")
print("=" * 60)

# a) Создание двумерного массива (3, 4) и сдвиг последнего столбца на место первого
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]], dtype=int)
print("\na) Исходный массив 3x4:")
print(a)

# Сдвигаем последний столбец на место первого (сдвиг по столбцам, ось=1)
a_rolled_cols = np.roll(a, shift=1, axis=1)
print("\nМассив после переноса последнего столбца на место первого (np.roll, axis=1):")
print(a_rolled_cols)

# b) Сдвиг последней строки на место первой
a_rolled_rows = np.roll(a, shift=1, axis=0)
print("\nb) Массив после переноса последней строки на место первой (np.roll, axis=0):")
print(a_rolled_rows)

# c) Создание второго массива и нахождение пересечения
c = np.array([[3, 4, 5, 6],
              [7, 8, 9, 10],
              [11, 12, 1, 2]], dtype=int)
print("\nc) Второй массив 3x4:")
print(c)

# Находим пересечение элементов (уникальные общие элементы)
intersection = np.intersect1d(a, c)
print("\nПересечение элементов массивов a и c (np.intersect1d):")
print(intersection)
print(f"Количество общих уникальных элементов: {len(intersection)}")

# d) Преобразование в одномерный массив с помощью flatten
d_flattened = c.flatten()
print("\nd) Одномерный массив на основе массива c (c.flatten()):")
print(d_flattened)
print(f"Форма: {d_flattened.shape}")

# e) Накопительная сумма элементов
e_cumsum = np.cumsum(d_flattened)
print("\ne) Накопительная сумма элементов (np.cumsum):")
print(e_cumsum)
print(f"Форма: {e_cumsum.shape}")

# f) Создание массива (2, 3) и добавление строки из единиц
f = np.array([[2, 4, 6],
              [8, 10, 12]], dtype=int)
print("\nf) Исходный массив 2x3:")
print(f)

# Добавляем строку из единиц
f_with_row = np.vstack([f, [1, 1, 1]])
print("\nМассив после добавления строки из единиц (np.vstack):")
print(f_with_row)
print(f"Форма: {f_with_row.shape}")

# g) Добавление столбца из десяток
g_with_col = np.hstack([f, [[10], [10]]])
print("\ng) Массив после добавления столбца из десяток (np.hstack):")
print(g_with_col)
print(f"Форма: {g_with_col.shape}")

# h) Накопительная сумма по строкам и столбцам
h_cumsum_rows = np.cumsum(f, axis=1)  # По строкам
h_cumsum_cols = np.cumsum(f, axis=0)  # По столбцам

print("\nh) Накопительная сумма элементов массива f:")
print("\nПо строкам (axis=1):")
print(h_cumsum_rows)
print("\nПо столбцам (axis=0):")
print(h_cumsum_cols)

# i) Натуральный логарифм элементов массива f
# Создаем копию с вещественным типом для вычисления логарифма
f_float = f.astype(float)
# Заменяем нули и отрицательные значения на 1 для безопасного вычисления логарифма
# В нашем массиве все значения положительные: [2, 4, 6, 8, 10, 12]
i_log = np.log(f_float)
print("\ni) Натуральный логарифм элементов массива f (np.log):")
print("Исходный массив f:")
print(f)
print("\nНатуральный логарифм каждого элемента:")
print(i_log)
print("\nПроверка (e^ln(x) = x):")
for i in range(f.shape[0]):
    for j in range(f.shape[1]):
        print(f"  ln({f[i, j]}) = {i_log[i, j]:.2f}, e^{i_log[i, j]:.2f} = {np.exp(i_log[i, j]):.2f}")

# j) Индексы минимальных элементов по строкам и столбцам
j_argmin_rows = np.argmin(f, axis=1)  # По строкам
j_argmin_cols = np.argmin(f, axis=0)  # По столбцам

print("\nj) Индексы минимальных элементов массива f:")
print("\nМассив f:")
print(f)

print("\nПо строкам (axis=1) - индекс столбца с минимальным значением в каждой строке:")
for i in range(f.shape[0]):
    min_val = f[i, j_argmin_rows[i]]
    print(f"  Строка {i}: минимальное значение {min_val} в столбце {j_argmin_rows[i]}")
print("Все индексы:", j_argmin_rows)

print("\nПо столбцам (axis=0) - индекс строки с минимальным значением в каждом столбце:")
for j in range(f.shape[1]):
    min_val = f[j_argmin_cols[j], j]
    print(f"  Столбец {j}: минимальное значение {min_val} в строке {j_argmin_cols[j]}")
print("Все индексы:", j_argmin_cols)

print("\n" + "=" * 60)
print("ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ О РЕЗУЛЬТАТАХ")
print("=" * 60)

# Сводная информация о всех результатах
results = [
    ("a (исходный)", a, "Исходный массив 3x4"),
    ("a_rolled_cols", a_rolled_cols, "Сдвиг столбцов"),
    ("a_rolled_rows", a_rolled_rows, "Сдвиг строк"),
    ("c", c, "Второй массив 3x4"),
    ("intersection", intersection, "Пересечение a и c"),
    ("d_flattened", d_flattened, "Массив c в 1D"),
    ("e_cumsum", e_cumsum, "Накоп. сумма d_flattened"),
    ("f (исходный)", f, "Массив 2x3"),
    ("f_with_row", f_with_row, "С добавленной строкой"),
    ("g_with_col", g_with_col, "С добавленным столбцом"),
    ("h_cumsum_rows", h_cumsum_rows, "Накоп. сумма по строкам"),
    ("h_cumsum_cols", h_cumsum_cols, "Накоп. сумма по столбцам"),
    ("f_float", f_float, "Массив f как float"),
    ("i_log", i_log, "Натуральный логарифм"),
]

print("\n{:20s} {:15s} {:25s} {:>10s} {:>10s}".format(
    "Операция", "Тип", "Форма", "Мин", "Макс"))
print("-" * 85)

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
    
    print("{:20s} {:15s} {:25s} {:>10s} {:>10s}".format(
        name, str(array.dtype), str(array.shape), min_val, max_val))


print("\n" + "=" * 60)
print("ВСЕ ОПЕРАЦИИ ВЫПОЛНЕНЫ УСПЕШНО")
print("=" * 60)
