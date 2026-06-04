import pandas as pd

# Путь к папке с файлами
FOLDER_PATH = r"C:\123\машинное обучение\практика 5\Lab5.3"

# a) Чтение файлов
df1 = pd.read_excel(f"{FOLDER_PATH}/Table_1.xlsx")
df2 = pd.read_excel(f"{FOLDER_PATH}/Table_2.xlsx")
df3 = pd.read_excel(f"{FOLDER_PATH}/Table_3.xlsx")

print("Данные успешно загружены.")

# b) Вертикальное объединение Table_1 и Table_3 (строки Table_1 сверху)
df_b = pd.concat([df1, df3], ignore_index=True)
df_b.to_excel(f"{FOLDER_PATH}/Table_b.xlsx", index=False)
print("Пункт b выполнен, сохранён в Table_b.xlsx")

# c) Внутреннее слияние Table_1 и Table_2 по столбцу 'id'
df_c = pd.merge(df1, df2, on='id', how='inner')
df_c.to_excel(f"{FOLDER_PATH}/Table_c.xlsx", index=False)
print("Пункт c выполнен, сохранён в Table_c.xlsx")

# d) Левое объединение Table_1 и Table_2 по столбцу 'id'
df_d = pd.merge(df1, df2, on='id', how='left')
df_d.to_excel(f"{FOLDER_PATH}/Table_d.xlsx", index=False)
print("Пункт d выполнен, сохранён в Table_d.xlsx")

# e) Внешнее слияние Table_1 и Table_2 по столбцу 'id'
df_e = pd.merge(df1, df2, on='id', how='outer')
df_e.to_excel(f"{FOLDER_PATH}/Table_e.xlsx", index=False)
print("Пункт e выполнен, сохранён в Table_e.xlsx")

# f) Левое объединение через set_index и join
df1_indexed = df1.set_index('id')
df2_indexed = df2.set_index('id')
df_f_indexed = df1_indexed.join(df2_indexed, how='left')
df_f = df_f_indexed.reset_index()  # возвращаем id как столбец
df_f.to_excel(f"{FOLDER_PATH}/Table_f.xlsx", index=False)
print("Пункт f выполнен, сохранён в Table_f.xlsx")
