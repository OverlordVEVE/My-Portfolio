import pandas as pd
import numpy as np
import json
import os
import sys
from pathlib import Path

# ------------------------------------------------------------
# 1. Задание пути к папке с данными
# ------------------------------------------------------------
FOLDER_PATH = r"C:\123\машинное обучение\практика 3\Lab3.3"

if not os.path.isdir(FOLDER_PATH):
    print(f"Ошибка: Папка {FOLDER_PATH} не найдена.")
    print("Пожалуйста, укажите правильный путь в переменной FOLDER_PATH.")
    sys.exit(1)

print("=" * 60)
print("Лабораторная работа №3. Чтение файлов с данными")
print("=" * 60)

# ------------------------------------------------------------
# a) Чтение файла iris_csv.csv
# ------------------------------------------------------------
iris_path = os.path.join(FOLDER_PATH, "iris_csv.csv")
if not os.path.exists(iris_path):
    iris_path = os.path.join(FOLDER_PATH, "iris_csv")

print("\n" + "-" * 40)
print("a) Чтение iris_csv.csv")
print("-" * 40)

try:
    iris_df = pd.read_csv(iris_path)
    print("Файл успешно загружен. Первые 5 строк:")
    print(iris_df.head())
    print("Размерность:", iris_df.shape)
    
    #  вывод всего содержимого файла iris_csv.csv -----
    # print("\n--- Полное содержимое файла iris_csv.csv ---")
    # with open(iris_path, 'r', encoding='utf-8') as f:
    #     print(f.read())
    # # -----------------------------------------------------------------------
    
except FileNotFoundError:
    print(f"Файл не найден: {iris_path}")
except Exception as e:
    print(f"Ошибка при чтении: {e}")

# ------------------------------------------------------------
# b) Чтение файла test_table.txt (без заголовков, разделитель пробелы)
# ------------------------------------------------------------
test_path = os.path.join(FOLDER_PATH, "test_table.txt")
print("\n" + "-" * 40)
print("b) Чтение test_table.txt")
print("-" * 40)

try:
    test_df = pd.read_csv(test_path, sep='\s+', header=None)
    print("Файл успешно загружен. Первые 5 строк:")
    print(test_df.head())
    print("Размерность:", test_df.shape)
    
    # вывод всего содержимого файла test_table.txt -----
    # print("\n--- Полное содержимое файла test_table.txt ---")
    # with open(test_path, 'r', encoding='utf-8') as f:
    #     print(f.read())
    # # -------------------------------------------------------------------------
    
except FileNotFoundError:
    print(f"Файл не найден: {test_path}")
except Exception as e:
    print(f"Ошибка при чтении: {e}")

# ------------------------------------------------------------
# c) Чтение листа Japan-1950 из Japan_stat_1950.xlsx
#    Данные начинаются с 7-й строки (пропускаем 5 пустых строк),
#    заголовки в строке 6 (после пропуска – строка 0), столбцы C:E.
# ------------------------------------------------------------
excel_path = os.path.join(FOLDER_PATH, "Japan_stat_1950.xlsx")
print("\n" + "-" * 40)
print("c) Чтение листа Japan-1950 из Japan_stat_1950.xlsx")
print("-" * 40)

excel_df = None
try:
    excel_df = pd.read_excel(
        excel_path,
        sheet_name="Japan-1950",
        skiprows=5,
        header=0,
        usecols="C:E",
        engine='openpyxl'
    )
    print("Лист Japan-1950 успешно загружен. Первые 5 строк:")
    print(excel_df.head())
    print("Размерность:", excel_df.shape)
    print("\nИнформация о столбцах:")
    print(excel_df.info())
    
    # вывод диапазона C6:E27 (строки 6-27, столбцы C,D,E) -----
    # print("\n--- Диапазон C6:E27 из листа Japan-1950 ---")
    # try:
    #     range_df = pd.read_excel(
    #         excel_path,
    #         sheet_name="Japan-1950",
    #         skiprows=5,        # пропускаем строки 1-5, строка 6 становится заголовком
    #         nrows=22,          # читаем 22 строки: строка 6 (заголовок) + 21 строка данных (7-27)
    #         usecols="C:E",
    #         engine='openpyxl'
    #     )
    #     print(range_df.to_string(index=False))
    # except Exception as e:
    #     print(f"Ошибка при чтении диапазона: {e}")
    # # -----------------------------------------------------------------------
    
except ImportError:
    print("Модуль openpyxl не установлен.")
    print("Для работы с Excel-файлами выполните в терминале:")
    print("  pip install openpyxl")
    print("После установки перезапустите скрипт.")
except ValueError as e:
    print(f"Ошибка при чтении Excel (возможно, неверное имя листа или параметры): {e}")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")

# ------------------------------------------------------------
# d) Чтение файла num_table.json (универсальный метод)
# ------------------------------------------------------------
json_path = os.path.join(FOLDER_PATH, "num_table.json")
print("\n" + "-" * 40)
print("d) Чтение num_table.json")
print("-" * 40)

json_df = None

def load_json_flexible(filepath):
    """Загружает JSON в DataFrame, пробуя различные форматы."""
    # Попытка 1: стандартный read_json
    try:
        df = pd.read_json(filepath)
        return df
    except ValueError:
        pass
    # Попытка 2: orient='records'
    try:
        df = pd.read_json(filepath, orient='records')
        return df
    except ValueError:
        pass
    # Ручная загрузка
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            if all(isinstance(row, list) for row in data):
                return pd.DataFrame(data)
            if all(isinstance(row, dict) for row in data):
                return pd.DataFrame(data)
        if isinstance(data, dict):
            if all(isinstance(v, list) for v in data.values()):
                lengths = [len(v) for v in data.values()]
                if len(set(lengths)) > 1:
                    print("Обнаружены списки разной длины. Обрезаем до минимальной.")
                    min_len = min(lengths)
                    trimmed = {k: v[:min_len] for k, v in data.items()}
                    return pd.DataFrame(trimmed)
                else:
                    return pd.DataFrame(data)
        return None
    except Exception:
        return None

if os.path.exists(json_path):
    json_df = load_json_flexible(json_path)
    if json_df is not None:
        print("JSON успешно преобразован в DataFrame. Первые 5 строк:")
        print(json_df.head())
        print("Размерность:", json_df.shape)
        
        # вывод всего содержимого JSON-файла -----
        # print("\n--- Полное содержимое файла num_table.json ---")
        # with open(json_path, 'r', encoding='utf-8') as f:
        #     print(f.read())
        # # ----------------------------------------------------------------
        
    else:
        print("Не удалось преобразовать JSON в DataFrame.")
        print("Проверьте структуру файла num_table.json.")
else:
    print(f"Файл не найден: {json_path}")

# ------------------------------------------------------------
# e) Последний столбец таблицы из num_table.json
# ------------------------------------------------------------
print("\n" + "-" * 40)
print("e) Последний столбец таблицы из num_table.json")
print("-" * 40)

if json_df is not None:
    last_col = json_df.iloc[:, -1]
    print("Последний столбец (первые 10 значений):")
    print(last_col.head(10))
    
    # повторный вывод всего JSON-файла (по желанию) -----
    # print("\n--- Полное содержимое файла num_table.json (повторно) ---")
    # with open(json_path, 'r', encoding='utf-8') as f:
    #     print(f.read())
    # # ---------------------------------------------------------------------------
    
else:
    print("Невозможно обратиться к столбцу — таблица не загружена.")

# ------------------------------------------------------------
# f) Первая строка таблицы из num_table.json
# ------------------------------------------------------------
print("\n" + "-" * 40)
print("f) Первая строка таблицы из num_table.json")
print("-" * 40)

if json_df is not None:
    first_row = json_df.iloc[0, :]
    print("Первая строка:")
    print(first_row)
    
    # ещё один вариант вывода исходного JSON -----
    # print("\n--- Полное содержимое файла num_table.json (ещё раз) ---")
    # with open(json_path, 'r', encoding='utf-8') as f:
    #     print(f.read())
    # # -----------------------------------------------------------------
    
else:
    print("Невозможно обратиться к строке — таблица не загружена.")

print("\n" + "=" * 60)
print("Скрипт завершён.")
print("=" * 60)