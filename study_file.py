"""Режими відкриття файлів"""
# "r" - Читиння (файл має існувати)
# "w" - Запис (створює новий файл або перезаписує інсуючий)
# "a" - Додавання (записує в кінець файлу)
# "rb" - Читання бінарного файлу
# "wb" - Запис у бінарний файл
# "r+" - Читання і запис (файл має існувати)
# "w+" - Запис і читання (перезаписує файл)





"""Типи файлів"""

"""1.Текстові файли"""
# .txt - Звичайний текстовий файл
# .csv - Таблиця, де дані розділені комами
# .json - Файл для збереження структурованих даних у форматі JSON (Аналог словника Python)
# .xml - Використовують для збереження структурованих даних, наприклад у веб-розробці
# .log - Файли журналів, що містять історію подій

"""Бінарні файли"""
# .jpg, .png, .gif - Зображення
# .mp3, .wav - Аудіофайли
# .mp4, .avi - Відеофайли
# .exe - Виконувані файли програм
# .zip, .rar - Архіви



with open("example/example.txt", "r") as file: # with ... as - Відкриває та закриває файл, зручно щоб потім не забути закрити файл
    file = file.read()
    print(file)

with open("example/example.txt", "w") as file:
    file.write("This is new text in file\n\n")
    file.write("Its also\n\n")

with open("example/example.txt", "a") as file:
    file.write("Third string\n\n")


with open("example/example.txt", "r") as file: #Читаємо файл по одному рядку
    line = file.readline()
    while line:
        print(line.strip()) # .strip() - Прибирає зайві переноси рядків
        line = file.readline()


with open("example/example.txt", "r") as file: # Читаємо всі рядки у список
    lines = file.readline()
    for line in lines:
        print(line.strip())

with open("image/image.jpg", "rb") as file: # Читання зображення в байтах
    content = file.read()
    print(type(content))

with open("image/copy_image.jpg", "wb") as file: # Запис у файл байтів минулого зображення
    file.write(content)


import csv

with open("example/data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"]
]

with open("example/data.csv", "w", newline="") as file:
    writer =csv.writer(file)
    writer.writerows(data)




import json

with open('example/data.json', 'r') as file:
    data = json.load(file)  # Завантажуємо дані в Python об'єкти (наприклад, словник)
    print(data)


data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

with open('example/output.json', 'w') as file:
    json.dump(data, file, indent=4)  # Додаємо indent для зручного відображення



"""Обробка великих файлів"""

with open("large_file.txt", "r") as file: # Замість того, щоб читати весь файл одразу, можна обробляти файл по частинах, наприклад, по рядках
    for line in file:
        print(line.strip())  # Обробка кожного рядка файлу

with open("large_output.txt", "w") as file: # Щоб записувати великі дані, можна використовувати схожу стратегію, обробляючи дані по частинах (наприклад, записуючи їх по шматках)
    for chunk in large_data:
        file.write(chunk)




"""Обробка помилок при роботі з файлами"""

try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Файл не знайдено!")
except PermissionError:
    print("Немає доступу до файлу!")
except Exception as e:
    print(f"Сталася непередбачена помилка: {e}")




"""Робота з архівами (ZIP, RAR)"""

import zipfile

# Розпакувати весь вміст архіву в поточну директорію
with zipfile.ZipFile("archive.zip", "r") as zip_ref:
    zip_ref.extractall()  # Розпаковка в поточну директорію

# Або можна отримати список файлів в архіві
with zipfile.ZipFile("archive.zip", "r") as zip_ref:
    print(zip_ref.namelist())


with zipfile.ZipFile("new_archive.zip", "w") as zip_ref:
    zip_ref.write("example.txt")  # Додавання файлу в архів

