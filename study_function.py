def say_hello(name):        # - Функція з одним параметром
    print(f"Hello, {name}")
say_hello("Alex")
say_hello("Oleg")
say_hello("Marko")

def add(a, b):              # - Функція з двома параметрами
    print(f"Suma: {a + b}")
add(3, 4)

def add(a, b):
    return a + b # return - повертає значення для функції, важливий, тому що, значення можна використовувати дальше в коді
result = add(3, 5)
print(result)
print(add(3, 5))


def greet(name="User"): # - Параметр за замовчуванням, який можна змінити
    print(f"Hallo, {name}")
greet()
greet("Max")

def sum_numbers(*number): # *args - Передає довільну кількість аргументів, переводить вказані елементи в кортеж
    return sum(number )
print(sum_numbers(1, 2, 4, 5, 876))

def print_args(*args):
    print(args)
print_args(1, True, "Hello")

def person_info(**info): # **args - Переводить будь-яку кількість аргументів в словник
    for key, value in info.items():
        print(f"{key}: {value}")
person_info(name="Ivan", age=25, city="Amsterdam")



"""Передача функцій у змінні"""
def greet(name):
    return f"Hello, {name}"

greeting = greet # - Зберігаємо функцію в змінну
print(greeting("Max"))


"""Вкладення функції(функція всередині функції)"""
def outer_function(msg):
    def inner_function():
        print(f"Message: {msg}")
    inner_function()

outer_function("Hello world!")


"""Замикання(Closures)"""
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)
print(double(5))
print(triple(5))



"""Анонімні функції(lambda)""" # Зручно використовувати коли потрібно записати невелику разову функцію
square = lambda x: x ** 2
print(square(4)) # 16


words = ["apple", "charry", "banana", "kivi"]
words.sort(key=lambda word: len(word)) # Сортування списку за довжиною слів
print(words)


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers)) # map() - застосовує функцію lambda до кожного елемента
print(squared)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # Виводить лише парні числа
print(even_numbers)

"""Декоратори"""
