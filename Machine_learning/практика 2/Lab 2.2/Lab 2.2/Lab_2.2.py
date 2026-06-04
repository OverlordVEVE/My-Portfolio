import numpy as np

# Настройка формата вывода
np.set_printoptions(precision=2, suppress=True)

print("=" * 60)
print("ПОЛЕЗНЫЕ НА ПРАКТИКЕ ФУНКЦИИ NUMPY")
print("=" * 60)

# a) Создание массива (7, 5) со случайными целыми [-10, 20) и сортировка по столбцам
a = np.random.randint(-10, 20, size=(7, 5))
print("\na) Исходный массив 7x5 со случайными целыми [-10, 20):")
print(a)
print(f"Форма: {a.shape}, Тип: {a.dtype}")

# Сортировка по столбцам (axis=0)
a_sorted = np.sort(a, axis=0)
print("\nМассив после сортировки по столбцам (np.sort, axis=0):")
print(a_sorted)

# b) Массив строк "Positive" и "Neg_or_0" на основе сравнения с 0
b_result = np.where(a > 0, "Positive", "Neg_or_0")
print("\nb) Массив строк на основе сравнения с 0 (a > 0):")
print(b_result)
print(f"Форма: {b_result.shape}, Тип: {b_result.dtype}")

# Подсчет количества положительных и неположительных элементов
positive_count = np.sum(a > 0)
neg_or_zero_count = np.sum(a <= 0)
print(f"Количество положительных элементов: {positive_count}")
print(f"Количество неположительных элементов: {neg_or_zero_count}")

# c) Массив строк с категориями
c_result = np.select(
    [
        a > 10,          # условие 1: больше 10
        (a >= 1) & (a <= 10),  # условие 2: от 1 до 10 включительно
        a < 0            # условие 3: меньше 0
    ],
    [
        "Big_pos",       # результат для условия 1
        "Small_pos",     # результат для условия 2
        "Negative"       # результат для условия 3
    ],
    default="Zero"       # значение по умолчанию (если ни одно условие не выполнено)
)

print("\nc) Массив строк с категориями:")
print(c_result)
print(f"Форма: {c_result.shape}, Тип: {c_result.dtype}")

# Подсчет элементов каждой категории
categories = ["Big_pos", "Small_pos", "Negative", "Zero"]
for category in categories:
    count = np.sum(c_result == category)
    print(f"  {category}: {count} элементов")

# d) Вычисление 25-го, 50-го и 75-го процентилей
percentiles = [25, 50, 75]
d_percentiles = np.percentile(a, percentiles)
print("\nd) Процентили массива a:")
for p_val, result in zip(percentiles, d_percentiles):
    print(f"  {p_val}-й процентиль: {result:.2f}")

# e) Медиана и стандартное отклонение
e_median = np.median(a)
e_std = np.std(a)
print("\ne) Статистические характеристики:")
print(f"  Медиана: {e_median:.2f}")
print(f"  Стандартное отклонение: {e_std:.2f}")

# f) Вычисление квантилей 0.2, 0.5, 0.7, 0.9
quantiles = [0.2, 0.5, 0.7, 0.9]
f_quantiles = np.quantile(a, quantiles)
print("\nf) Квантили массива a:")
for q_val, result in zip(quantiles, f_quantiles):
    print(f"  {q_val:.1f}-й квантиль: {result:.2f}")

print("\n" + "=" * 60)
print("ДОПОЛНИТЕЛЬНАЯ СТАТИСТИЧЕСКАЯ ИНФОРМАЦИЯ")
print("=" * 60)

# Полная статистика массива
print("\nПолная статистика массива a:")
print("-" * 40)
print(f"Минимум: {np.min(a)}")
print(f"Максимум: {np.max(a)}")
print(f"Среднее: {np.mean(a):.2f}")
print(f"Медиана: {np.median(a):.2f}")
print(f"Стандартное отклонение: {np.std(a):.2f}")
print(f"Дисперсия: {np.var(a):.2f}")
print(f"Размах: {np.ptp(a)}")

print("\nРаспределение значений:")
print("-" * 40)
print(f"Всего элементов: {a.size}")
print(f"Отрицательных (<0): {np.sum(a < 0)} ({np.mean(a < 0)*100:.1f}%)")
print(f"Нулевых (=0): {np.sum(a == 0)} ({np.mean(a == 0)*100:.1f}%)")
print(f"Положительных (>0): {np.sum(a > 0)} ({np.mean(a > 0)*100:.1f}%)")
print(f"Малых положительных [1, 10]: {np.sum((a >= 1) & (a <= 10))} ({np.mean((a >= 1) & (a <= 10))*100:.1f}%)")
print(f"Больших положительных (>10): {np.sum(a > 10)} ({np.mean(a > 10)*100:.1f}%)")

print("\n" + "=" * 60)
print("ВИЗУАЛИЗАЦИЯ СОРТИРОВКИ")
print("=" * 60)

print("\nСравнение исходного и отсортированного массивов:")
print("\nИсходный массив a (первые 3 строки):")
print(a[:3])
print("\nОтсортированный по столбцам (первые 3 строки):")
print(a_sorted[:3])
print("\nРазница между отсортированным и исходным:")
print("(значения показывают, на сколько изменилась позиция элемента)")
# Для наглядности покажем первые 3 строки разницы
print(np.abs(a[:3] - a_sorted[:3]))

print("\n" + "=" * 60)
print("СРАВНЕНИЕ ПРОЦЕНТИЛЕЙ И КВАНТИЛЕЙ")
print("=" * 60)

print("\nСравнение процентилей и соответствующих квантилей:")
print("-" * 50)
print(f"{'Процентиль':<15} {'Значение':<15} {'Соответствующий квантиль':<25}")
print("-" * 50)

# Создаем соответствие между процентилями и квантилями
percentile_quantile_pairs = [
    (25, 0.25),
    (50, 0.50),
    (75, 0.75)
]

for p_val, q_val in percentile_quantile_pairs:
    percentile_val = np.percentile(a, p_val)
    quantile_val = np.quantile(a, q_val)
    print(f"{p_val}% ({q_val})    {percentile_val:>10.2f}     {quantile_val:>10.2f}")

# Добавляем квантили из пункта f
print("\nДополнительные квантили из пункта f:")
for q_val in [0.2, 0.7, 0.9]:
    quantile_val = np.quantile(a, q_val)
    print(f"  {q_val:.1f}-й квантиль: {quantile_val:.2f}")

print("\n" + "=" * 60)
print("ПРАКТИЧЕСКОЕ ПРИМЕНЕНИЕ РЕЗУЛЬТАТОВ")
print("=" * 60)

print("\nНа основе анализа массива a можно сделать выводы:")
print("-" * 60)

# Анализ распределения
mean_val = np.mean(a)
median_val = np.median(a)
std_val = np.std(a)

print(f"1. Среднее значение: {mean_val:.2f}")
print(f"2. Медиана: {median_val:.2f}")

if mean_val > median_val:
    print("   Распределение сдвинуто вправо (положительная асимметрия)")
elif mean_val < median_val:
    print("   Распределение сдвинуто влево (отрицательная асимметрия)")
else:
    print("   Распределение симметрично")

print(f"\n3. Стандартное отклонение: {std_val:.2f}")
print(f"   Коэффициент вариации: {(std_val/abs(mean_val)*100 if mean_val != 0 else '∞'):.1f}%")

print("\n4. Интерквартильный размах (IQR):")
q1 = np.percentile(a, 25)
q3 = np.percentile(a, 75)
iqr = q3 - q1
print(f"   Q1 (25%): {q1:.2f}")
print(f"   Q3 (75%): {q3:.2f}")
print(f"   IQR: {iqr:.2f}")

# Определение выбросов
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = a[(a < lower_bound) | (a > upper_bound)]

print(f"\n5. Выбросы (значения за пределами Q1-1.5*IQR и Q3+1.5*IQR):")
print(f"   Нижняя граница: {lower_bound:.2f}")
print(f"   Верхняя граница: {upper_bound:.2f}")
print(f"   Количество выбросов: {len(outliers)}")
if len(outliers) > 0:
    print(f"   Значения выбросов: {outliers.flatten()}")

print("\n" + "=" * 60)
print("ВСЕ ФУНКЦИИ ПРИМЕНЕНЫ УСПЕШНО")
print("=" * 60)
