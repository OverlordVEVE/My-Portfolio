import numpy as np

# Настройка формата вывода
np.set_printoptions(precision=2, suppress=True)

print("=" * 60)
print("СТРУКТУРИРОВАННЫЕ МАССИВЫ NUMPY И ДОПОЛНИТЕЛЬНЫЕ ФУНКЦИИ")
print("=" * 60)

# a) Создание структурированного массива с информацией об автомобилях
print("\na) Создание структурированного массива с информацией об автомобилях:")

# Определяем структуру массива
dtype = [
    ('model', 'U20'),      # Название модели (строка Unicode до 20 символов)
    ('power', 'i4'),       # Мощность двигателя (целое 4 байта)
    ('color', 'U10'),      # Цвет кузова (строка Unicode до 10 символов)
    ('price', 'f4')        # Стоимость (вещественное 4 байта)
]

# Создаем массив с данными
cars = np.array([
    ('Toyota Camry', 203, 'Black', 28000.5),
    ('Toyota Corolla', 132, 'White', 21000.0),
    ('Toyota RAV4', 203, 'Red', 32000.0),
    ('Toyota Highlander', 295, 'Silver', 45000.0),
    ('Toyota Prius', 121, 'Blue', 27000.0),
    ('Toyota Tacoma', 278, 'Black', 35000.0),
    ('Toyota 4Runner', 270, 'Gray', 42000.0),
    ('Toyota Sienna', 296, 'White', 38000.0)
], dtype=dtype)

print("Структурированный массив автомобилей Toyota:")
print(cars)
print(f"\nТип данных массива: {cars.dtype}")
print(f"Форма массива: {cars.shape}")
print(f"Количество записей: {len(cars)}")

# Выводим данные в удобном формате
print("\nДетальная информация об автомобилях:")
print("-" * 60)
print(f"{'№':<3} {'Модель':<20} {'Мощность':<10} {'Цвет':<10} {'Стоимость':<10}")
print("-" * 60)
for i, car in enumerate(cars):
    print(f"{i+1:<3} {car['model']:<20} {car['power']:<10} {car['color']:<10} ${car['price']:<10.2f}")

# b) Обращение к записям с определенным цветом кузова
print("\n\nb) Автомобили с черным цветом кузова (color == 'Black'):")
black_cars = cars[cars['color'] == 'Black']
print(black_cars)
print(f"Количество черных автомобилей: {len(black_cars)}")

print("\nАвтомобили с белым цветом кузова (color == 'White'):")
white_cars = cars[cars['color'] == 'White']
print(white_cars)
print(f"Количество белых автомобилей: {len(white_cars)}")

# c) Названия моделей со стоимостью выше 30000
print("\n\nc) Названия моделей со стоимостью выше $30,000 (price > 30000):")
expensive_models = cars[cars['price'] > 30000]['model']
print("Модели:", expensive_models)
print(f"Количество дорогих моделей: {len(expensive_models)}")

# d) Стоимость автомобилей с мощностью двигателя выше 250 л.с.
print("\n\nd) Стоимость автомобилей с мощностью двигателя > 250 л.с. (power > 250):")
powerful_cars_prices = cars[cars['power'] > 250]['price']
print("Стоимость мощных автомобилей:", powerful_cars_prices)
print(f"Средняя стоимость мощных автомобилей: ${np.mean(powerful_cars_prices):.2f}")

# e) Сохранение структурированного массива в файл .npy
print("\n\ne) Сохранение структурированного массива в файл 'cars_data.npy':")
np.save('cars_data.npy', cars)
print("Файл успешно сохранен!")

# Проверка загрузки файла
loaded_cars = np.load('cars_data.npy', allow_pickle=True)
print(f"Файл загружен обратно. Количество записей: {len(loaded_cars)}")
print("Первые 3 записи из загруженного файла:")
print(loaded_cars[:3])

# f) Создание двумерного массива (3, 4) и преобразование в int64
print("\n\nf) Создание двумерного массива (3, 4) и преобразование в int64:")
f_array = np.random.random((3, 4))
print("Исходный массив со случайными числами [0, 1):")
print(f_array)
print(f"Форма: {f_array.shape}, Тип: {f_array.dtype}")

f_array_int64 = f_array.astype(np.int64)
print("\nМассив после преобразования в int64 (значения умножаются на 1 для наглядности):")
# Умножаем на 100 для получения более интересных целых чисел
f_array_int64 = (f_array * 100).astype(np.int64)
print(f_array_int64)
print(f"Форма: {f_array_int64.shape}, Тип: {f_array_int64.dtype}")

# g) Преобразование массива в обычный список Python
print("\n\ng) Преобразование массива в обычный список Python:")
f_list = f_array_int64.tolist()
print("Результат преобразования:")
print(f_list)
print(f"Тип результата: {type(f_list)}")
print(f"Тип первого элемента: {type(f_list[0])}")
print(f"Тип первого элемента первого вложенного списка: {type(f_list[0][0])}")

# h) Добавление новой оси с помощью expand_dims
print("\n\nh) Добавление новой оси с помощью expand_dims (форма (3, 1, 4)):")
h_array = np.expand_dims(f_array_int64, axis=1)
print("Массив после np.expand_dims(array, axis=1):")
print(h_array)
print(f"Форма: {h_array.shape}, Тип: {h_array.dtype}")

# i) Перестановка осей массива
print("\n\ni) Перестановка осей массива с помощью transpose:")
# Меняем местами строки и столбцы (ось 0 и ось 1)
i_array = np.transpose(f_array_int64, (1, 0))
print("Массив после np.transpose(array, (1, 0)):")
print(i_array)
print(f"Форма: {i_array.shape}, Тип: {i_array.dtype}")

# Альтернативный способ - метод .T
print("\nАльтернативный способ - использование метода .T (транспонирование):")
i_array_T = f_array_int64.T
print(i_array_T)
print(f"Форма: {i_array_T.shape}")

# j) Создание массива формы (1, 2, 1, 5, 3) и получение массива формы (2, 5, 3)
print("\n\nj) Создание массива формы (1, 2, 1, 5, 3) и преобразование в (2, 5, 3):")
j_array = np.zeros((1, 2, 1, 5, 3), dtype=np.float32)
print(f"Исходный массив формы {j_array.shape}:")
print("(выводим первую матрицу 5x3 из первого блока):")
print(j_array[0, 0, 0])  # Первая матрица 5x3

# Удаляем оси с размерностью 1 с помощью squeeze
j_array_squeezed = np.squeeze(j_array)
print(f"\nМассив после np.squeeze() (удалены оси с размерностью 1):")
print("Форма:", j_array_squeezed.shape)
print("Первая матрица 5x3:")
print(j_array_squeezed[0])

print("\n" + "=" * 60)
print("ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ СТРУКТУРИРОВАННОГО МАССИВА")
print("=" * 60)

# Анализ данных об автомобилях
print("\nСтатистика по автомобилям Toyota:")
print("-" * 40)

print(f"Общее количество моделей: {len(cars)}")
print(f"Средняя мощность: {np.mean(cars['power']):.1f} л.с.")
print(f"Максимальная мощность: {np.max(cars['power'])} л.с. ({cars[np.argmax(cars['power'])]['model']})")
print(f"Минимальная мощность: {np.min(cars['power'])} л.с. ({cars[np.argmin(cars['power'])]['model']})")
print(f"Средняя стоимость: ${np.mean(cars['price']):.2f}")
print(f"Общая стоимость всех автомобилей: ${np.sum(cars['price']):.2f}")

print("\nРаспределение по цветам:")
colors, counts = np.unique(cars['color'], return_counts=True)
for color, count in zip(colors, counts):
    percentage = count / len(cars) * 100
    print(f"  {color}: {count} автомобилей ({percentage:.1f}%)")

print("\nАвтомобили, сгруппированные по диапазонам мощности:")
power_ranges = [
    ("До 150 л.с.", cars[cars['power'] < 150]),
    ("150-200 л.с.", cars[(cars['power'] >= 150) & (cars['power'] < 200)]),
    ("200-250 л.с.", cars[(cars['power'] >= 200) & (cars['power'] < 250)]),
    ("250+ л.с.", cars[cars['power'] >= 250])
]

for range_name, range_cars in power_ranges:
    if len(range_cars) > 0:
        avg_price = np.mean(range_cars['price'])
        print(f"  {range_name}: {len(range_cars)} авто, средняя цена: ${avg_price:.2f}")

print("\n" + "=" * 60)
print("СРАВНЕНИЕ ФОРМ МАССИВОВ ИЗ ПУНКТОВ f-j")
print("=" * 60)

arrays_info = [
    ("f_array", f_array, "Исходный массив 3x4"),
    ("f_array_int64", f_array_int64, "Преобразованный в int64"),
    ("h_array", h_array, "После expand_dims (3,1,4)"),
    ("i_array", i_array, "После transpose (4,3)"),
    ("j_array", j_array, "Массив zeros (1,2,1,5,3)"),
    ("j_array_squeezed", j_array_squeezed, "После squeeze (2,5,3)")
]

print("\n{:20s} {:25s} {:15s} {:>15s}".format(
    "Имя массива", "Форма", "Тип данных", "Размер"))
print("-" * 80)

for name, array, description in arrays_info:
    print("{:20s} {:25s} {:15s} {:>15d}".format(
        name, str(array.shape), str(array.dtype), array.size))

print("\n" + "=" * 60)

print("\n" + "=" * 60)
print("ВСЕ ОПЕРАЦИИ ВЫПОЛНЕНЫ УСПЕШНО")
print("=" * 60)
