empty_set = set() # - Порожня множина

numbers = {1, 2, 3, 4, 5}

unique_numbers = {1, 2, 2, 3, 4, 4, 5, 6, 6} # - Зберігає значення без повторювань
print(unique_numbers)

letters = set("hello") # - Робить сет з символів в довільному порядку
print(letters)

s = {1, 2, 3}
s.add(4) # .add() - Додає елемент
s.remove(2) # .remove() - Видаляє елемент
s.discard(10) # .discard() - Видаляє елемент, але якщо елемента не виявлено, то помилки НЕ буде
s_pop = s.pop() # .pop() - Видаляє і повертає довільний елемент
copy_s = s.copy() # .copy() - Створює копію множини
s.clear() # .clear() - Очищує множину

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b) # "|" - Об'єднання сетів: {1, 2, 3, 4, 5, 6}
print(a.union(b)) # - {1, 2, 3, 4, 5, 6}

print(a & b) # "&" - Перетин сетів: {3, 4}
print(a.intersection(b)) # - {3, 4}

print(a - b) # "-" - Різниця сетів: {1, 2}
print(a.difference(b)) # - {1, 2}

print(a ^ b) # "^" - Симетрична різниця сетів: {1, 2, 5, 6}
print(a.symmetric_difference(b)) # - {1, 2, 5, 6}

if 3 in a:
    print("Is in set")


a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b)) # True (Немає спільних елементів)

len(a) # - Кількість елементів у множині
sorted(a) # - Сортує множину та повертає список

"""Перевірка підмножин"""
small = {1, 2}
big = {1, 2, 3, 4}
print(small.issubset(big)) # - True
print(big.issuperset(small)) # - True