empty_dict = {}

numbers = {1: "one", 2: "two", 3: "three"}
person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

print(person["name"])
print(person["age"]) # - Якщо не буде значення виникне помилка
print(person.get("job", "Not Found")) # .get() - Якщо немає значення то виведе текст

person["job"] = "Developer" # - Додаємо нові дані
person["age"] = 26 # - Змінюємо значення

del person["city"] # - Видаляє ключ

removed_value = person.pop("age") # .pop() - Видаляє ключ та повертає його значення
print(removed_value)

for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

print(person.keys()) # - Всі ключі
print(person.values()) # - Всі значення
print(person.items()) # - Всі пари (ключ, значення)

if "name" in person:
    print("Key found") # - Перевірка наявності ключа

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2) # - Обєднання двох словників
print(dict1)

original = {"a": 1, "b": 2}
copy_dict = original.copy() # .copy() - Обовязково використовувати щоб зміни на копії не вплинули на оригінал

person.clear() # .clear() - Очищує повністю словник
print(person)

age = person.get("age", 18) # - Якщо "age" немає то повертає 18

removed_value = person.pop("age", "Not Found") # - Якщо "age" є - повертає його значення, якщо ні то виводить вказаний текст
print(removed_value)

last_item = person.popitem() # Видалення останнього елемента
print(last_item)

"""Створення словника за допомогою fromkeys()"""
keys = ["name", "age", "city"]
default_value = "Unknown"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

for value in person.values(): # Перебір лише значень
    print(value)


"""Перетворення списку пар у словник"""
pairs = [("name", "John"), ("age", 25)]
person = dict(pairs)
print(person)