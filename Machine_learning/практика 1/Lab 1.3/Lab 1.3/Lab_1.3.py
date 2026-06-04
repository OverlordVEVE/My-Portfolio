import numpy as np
from numpy import random

# Настройка формата вывода
np.set_printoptions(precision=2, suppress=True)

print("=" * 60)
print("РАЗЛИЧНЫЕ ОПЕРАЦИИ С МАССИВАМИ")
print("=" * 60)

# a) Создание двумерного массива с целыми числами
a = np.array([[2, 5, 8, 11],
              [3, 6, 9, 12],
              [4, 7, 10, 13]], dtype=int)
print("\na) Двумерный массив с целыми числами:")
print(a)
print(f"Форма: {a.shape}, Тип: {a.dtype}")

# b) Сложение массива с числом 7
b_result = a + 7
print("\nb) Сложение массива a с числом 7 (a + 7):")
print(b_result)

# c) Умножение массива на число 3.5
c_result = a * 3.5
print("\nc) Умножение массива a на число 3.5 (a * 3.5):")
print(c_result)

# d) Остаток от деления массива на число 3
d_result = a % 3
print("\nd) Остаток от деления массива a на число 3 (a % 3):")
print(d_result)

# e) Целочисленное деление массива на число 4
e_result = a // 4
print("\ne) Целочисленное деление массива a на число 4 (a // 4):")
print(e_result)

# f) Создание двумерного массива (4, 5) со случайными числами [0, 1)
f_2d = np.random.random((4, 5))
print("\nf1) Двумерный массив 4x5 со случайными числами [0, 1):")
print(f_2d)
print(f"Форма: {f_2d.shape}, Тип: {f_2d.dtype}")

# f) Создание одномерного массива с 5 вещественными элементами
f_1d = np.array([1.5, 2.3, 3.7, 4.1, 5.9], dtype=float)
print("\nf2) Одномерный массив с 5 вещественными элементами:")
print(f_1d)
print(f"Форма: {f_1d.shape}, Тип: {f_1d.dtype}")

# g) Сложение массивов с помощью функции add
g_result = np.add(f_2d, f_1d)
print("\ng) Сложение массивов с помощью функции add (np.add(f_2d, f_1d)):")
print("Двумерный массив + одномерный массив (broadcasting):")
print(g_result)

# h) Вычитание одномерного массива из двумерного
h_result = f_2d - f_1d
print("\nh) Вычитание одномерного массива из двумерного (f_2d - f_1d):")
print(h_result)

# i) Перемешивание элементов каждого массива
# Создаем копии для перемешивания
f_2d_shuffled = f_2d.copy()
f_1d_shuffled = f_1d.copy()

random.shuffle(f_2d_shuffled)  # Перемешиваем строки
random.shuffle(f_1d_shuffled)  # Перемешиваем элементы

print("\ni1) Двумерный массив после перемешивания строк:")
print(f_2d_shuffled)

print("\ni2) Одномерный массив после перемешивания элементов:")
print(f_1d_shuffled)

# j) Нахождение суммы элементов массивов с помощью reduce и add
j_sum_2d = np.add.reduce(f_2d.flatten())  # Сумма всех элементов двумерного массива
j_sum_1d = np.add.reduce(f_1d)  # Сумма всех элементов одномерного массива

print("\nj) Сумма элементов массивов с помощью np.add.reduce():")
print(f"Сумма всех элементов двумерного массива: {j_sum_2d:.2f}")
print(f"Сумма всех элементов одномерного массива: {j_sum_1d:.2f}")

print("\n" + "=" * 60)
print("ВСЕ ОПЕРАЦИИ ВЫПОЛНЕНЫ УСПЕШНО")
print("=" * 60)

# Дополнительная информация
print("\n" + "-" * 60)
print("СРАВНЕНИЕ РЕЗУЛЬТАТОВ:")
print("-" * 60)

print("\nИсходный двумерный массив a:")
print(a)

print("\nОперации с массивом a:")
operations = [
    ("a + 7", b_result),
    ("a * 3.5", c_result),
    ("a % 3", d_result),
    ("a // 4", e_result)
]

for name, result in operations:
    print(f"\n{name}:")
    print(result)

print("\n" + "-" * 40)
print("ОПЕРАЦИИ С МАССИВАМИ ИЗ ПУНКТА f:")
print("-" * 40)

print("\nИсходные массивы:")
print("Двумерный массив:")
print(f_2d)
print("\nОдномерный массив:")
print(f_1d)

print("\nРезультаты операций:")
print("Сложение (broadcasting):")
print(g_result)
print("\nВычитание (broadcasting):")
print(h_result)

print("\n" + "=" * 60)
print("ПРОВЕРКА ТИПОВ ДАННЫХ:")
print("=" * 60)

arrays_info = [
    ("a", a, "Исходный целочисленный массив"),
    ("b_result", b_result, "a + 7"),
    ("c_result", c_result, "a * 3.5"),
    ("d_result", d_result, "a % 3"),
    ("e_result", e_result, "a // 4"),
    ("f_2d", f_2d, "Двумерный случайный массив"),
    ("f_1d", f_1d, "Одномерный вещественный массив"),
    ("g_result", g_result, "f_2d + f_1d"),
    ("h_result", h_result, "f_2d - f_1d"),
]

print("\n{:20s} {:15s} {:20s} {:>10s} {:>10s}".format(
    "Имя", "Тип", "Форма", "Мин", "Макс"))
print("-" * 80)

for name, array, description in arrays_info:
    if array.dtype in [np.float32, np.float64]:
        min_val = f"{array.min():.2f}"
        max_val = f"{array.max():.2f}"
    else:
        min_val = f"{array.min():.0f}"
        max_val = f"{array.max():.0f}"
    
    print("{:20s} {:15s} {:20s} {:>10s} {:>10s}".format(
        name, str(array.dtype), str(array.shape), min_val, max_val))
