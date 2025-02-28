"""Списки та операції з ними"""

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(list_of_numbers[0])
print(list_of_numbers[-1])

list_of_numbers[3] = 10
print(list_of_numbers)

list_of_numbers.append(4) # Додає елемент в кінець списку
print(list_of_numbers)

list_of_numbers.insert(1, 9) # Втавляє елемент під заданий індекс
print(list_of_numbers)

list_of_numbers.remove(4)
print(list_of_numbers)

pop_list = list_of_numbers.pop(1) # Видаляє елемент та повертає його значення
print(pop_list)
print(list_of_numbers)

my_list = [1, 2, 3, 4, 5, 4]
copy_list = my_list
del copy_list[1:3] # Видаляє елемент або цілий блок списку
print(copy_list)

mini_list = my_list[1:4] # Дозволяє вибрати підсписок елементів з 1 по 4 (не включаючи 4)
print(mini_list)

every_second_items = my_list[::2] # Вибирає кожен другий елемент
print(every_second_items)

my_list = [1, 2, 3, 4, 5, 2]
print(my_list.count(3)) # count() - Показує кількість входжень певного елемента в список

print(my_list.index(3)) # index() - Показує індекс певного елемента списку

my_list.sort() # sort() - Сортує список за замовчуванням від найменшого до найбільшого
print(my_list)

my_list.reverse() # reserve() - Перевертає список навпаки
print(my_list)

my_list.clear() # clear() - Очищує повністю список
print(my_list)



"""Мішані списки"""

words = ["apple", "banana", "cherry", "date"]
print(words[1])
print(words[-1])

mixed = [1, 2, "apple", 3, "banana"]
print(mixed[2])

sum_numbers = 0
for i in mixed:
    if isinstance(i, int):
        sum_numbers += i
print(sum_numbers)

"""Перевірка типів елементів в змішаному списку"""
mixed = [1, "hello", 3.5, [1, 2, 3], True]
for i in mixed:
    if isinstance(i, str):
        print(f"String: {i}")
    elif isinstance(i, int):
        print(f"Integer: {i}")
    elif isinstance(i, bool):
        print(f"Bool: {i}")
    elif isinstance(i, list):
        print(f"List: {i}")
    elif isinstance(i, float):
        print(f"Float: {i}")


"""Перетворення всіх елементів у верхній регістр"""
words = ["apple", "banana", "cherry"]
upper_words = [word.upper() for word in words]
print(upper_words)


"""Перевірка на наявність елементів"""
words = ["apple", "banana", "cherry", "date"]
if "banana" in words:
    print("Found \"Banana\" in list.")

index = words.index("cherry")
print(f"Index of 'cherry': {index}")


"""Сортування списку з рядками"""
words = ["apple", "banana", "date", "cherry"]
words.sort()
print(words)

words.sort(reverse=True)
print(words)


"""Обєднання списків"""
list1 = ["Apple", "Tomato"]
list2 = ["Orange", "Avocado"]
total_list = list1 + list2
print(total_list)

list1 = ["Apple", "Tomato"]
list2 = ["Orange", "Avocado"]
list1.extend(list2)
print(list1)


"""Перевірка на порожній список"""
fruits = []
if not fruits:
    print("List dont have anithing")
else:
    print("List have items!")

"""Переьворення перших символів рядка на великі"""
fruits = ["Orange", "Apple", "Blubery", "Kivi", "Grape"]
for i in range(len(fruits)):
    fruits[i] = fruits[i][0]
print(fruits)


"""Виводить лише ті слова зі списку які починаються на певну літеру"""
list_of_word = ["have", "apple", "name", "password", "ananas", "orange", "avocado", "Tolik", "globus", "banana"]
start_a_list = []
for i in list_of_word:
    if i.startswith("a"):
        start_a_list.append(i)
print(start_a_list)
