my_string = "Hello"

print(len(my_string)) # len() - Виводить довжину рядка
print(my_string.upper()) # .upper() - Робить всі літери великими
print(my_string.lower()) # .lower() - Робить всі літери маленькими

my_string = "  Hello  "
print(my_string.strip()) # .strip() - Забирає пробіли на початку та в кінці
print(my_string.lstrip()) # .lstrip() - Забирає пробіли на початку
print(my_string.rstrip()) # .rstrip() - Забирає пробіли в кінці

my_string = "Hello"
new_string = my_string.replace("Hello", "Hi") # .replace() - Замінює слово іншим
print(new_string)

words = "apple,banana,cherry".split(",") # .split() - Робить з рядка список з розділенням на вписаному елементі
print(words)

words = ['apple', 'banana', 'cherry']
joined_string = ", ".join(words) # .join() - Обєднує список в рядок з вказаним розділенням
print(joined_string)

print(my_string.find("e")) # .find() - Знаходить перше входження елемента в рядок та виводить його індекс, а якщо ні то виводить -1
print(my_string.rfind("o")) # .rfind() - Шукає останнє входження елемента в рядок та виводить його індекс, а якщо ні то виводить -1
print(my_string.index("o")) # .index() - Працює як find() але якщо елемента немає то видає помилку

print(my_string.count("o")) # .count() - Рахує кількість вказаних елементів в рядку

print(my_string.startswith("He")) # .startswith() - Перевіряє чи починається рядок на вказаний підрядок

print(my_string.endswith("o")) # .endswith() - Перевіряє чи закінчується рядок на певний підрядок

name = "Alex"
age = 25
inf = "Hallo {}, are you have {} years old?".format(name, age) # .format() - Аналог f"" рядків, підходить для версій Python нижче 3.6
print(inf)


text = "hello world"
print(text.capitalize()) # .capitalize() - Робить першу літеру рядка великою

text = "hello world"
print(text.title()) # .title() - Робить першу літеру кожного рядка великою

text = "Hello World"
print(text.swapcase()) # .swapcase() - Замінює великі букви - малими, а малі - великими

number = "42"
print(number.zfill(5)) # .zfill() - Додає нулі на початку рядку щоб рядок мав задану довжину

print("123".isdigit()) # .isdigit() - Перевіряє чи складається рядок лише з цифр
print("abc".isdigit()) # .isdigit() - False

print("Hello".isalpha()) # .isalpha() - Перевіряє чи складається рядок лише з букв
print("Hallo123".isalpha()) # .isalpha() - False

"""Робота з багатомовними рядками та кодуваннями"""
text = "Hello"
encode_text = text.encode("utf-8") # .encode("utf-8") - Перетворює рядок в байти з певним кодуванням
print(encode_text)

byte_text = b"Hello"
decode_text = byte_text.decode("utf-8") # .decode("utf-8") - Перетворює байти назад у рядок
print(decode_text)

"""Регулярні вирази"""
import re
text = "The rain in Spain falls mainly in the plain."
pattern = r"\bin\b" # - Шукає слово "in"
matches = re.findall(pattern, text)
print(matches) # - Виведе['in', 'in']