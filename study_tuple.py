empty_tuple = () # - Порожній кортеж

single_tuple = (42,) # - Потрібна кома навіть якщо елемент один

fruits = ("apple", "banana", "cherry")

mixed = (1, "hallo", 3.14, True)

numbers = 1, 2, 3, 4 # - Кортеж без дужок, додаються автоматично

fruits = ("apple", "banana", "cherry")
print(fruits[0])
print(fruits[-1])

for fruit in fruits:
    print(fruit)

a = (1, 2, 3)
b = (4, 5, 6)

c = a + b
print(c)

d = a * 2
print(d)

print(2 in a) #Перевірка на наявність елемента

"""Розпаковка кортежу"""
point = (3, 5)
x, y = point # x = 3, y = 5

a, *b = (1, 2, 3, 4)
print(a) # 1
print(b) # [2, 3, 4]

number = (1, 4, 5, 2, 1, 8)
print(number.count(1)) # Перевіряє кількість входжень певного елемента в кортеж
print(number.index(3)) # Перевіряє індекс першого входження