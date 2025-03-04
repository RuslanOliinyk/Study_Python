# Створення класу
class Car:
    def __init__(self, brand, model, year): # Конструктор класу
        self.brand = brand # Атрибути об'єкта
        self.model = model
        self.year = year

    def display_info(self): # Метод класу
        print(f"{self.brand} {self.model}, {self.year}")

# Створення об'єкта
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("BMW", "X5", 2023)

# Виклик методу
car1.display_info() # Виведе: Toyota Camry, 2022
car2.display_info() # Виведе: BMW X5, 2023



"""Наслідування""" # Наслідування дозволяє створювати нові класи на основі вже існуючих.
# Базовий клас
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some generic sound")

# Похідний клас
class Dog(Animal):
    def make_sound(self): # Перевизначаємо метод
        print("Woof! Woof!")

# Використання
dog = Dog("Buddy")
dog.make_sound() # Виведе: Woof! Woof!


"""Поліморфізм""" # Дозволяє об'єктам різних класів мати однакові методи, але з різною реалізацією.
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Використання поліморфізму
animals = [Dog("Rex"), Cat("Whiskers")]

for animal in animals:
    animal.make_sound()



"""Інкапсуляція""" # Обмежує доступ до певних даних у класі, щоб захистити їх від прямої зміни.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Приватний атрибут

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance  # Метод для доступу до балансу

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Виведе: 1500


"""Статичні та класові методи"""
# Статичні методи (@staticmethod) – не використовують self і не змінюють стан об'єкта або класу.
# Класові методи (@classmethod) – використовують cls, щоб працювати з самим класом

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        return f"This is a {cls.__name__} class"

# Використання статичного методу
print(MathUtils.add(3, 5))  # Виведе: 8

# Використання класового методу
print(MathUtils.info())  # Виведе: This is a MathUtils class

# @staticmethod дозволяє викликати метод без створення екземпляра класу.
# @classmethod працює з класом, а не з конкретним об'єктом.


"""Магічні методи (__str__, __len__, __eq__ та інші)"""

class User:
    def __init__(self, name, gmail):
        self.name = name
        self.gmail = gmail

    def __str__(self):
        return f"User: {self.name}, Email: {self.gmail}"

user1 = User("John", "john@example.com")
print(user1)  # Виведе: User: John, Email: john@example.com

# __str__ задає, як буде виглядати об'єкт при print(user1)


class User:
    def __init__(self, name, gmail):
        self.name = name
        self.gmail = gmail

    def __eq__(self, other):
        return self.gmail == other.gmail  # Порівнюємо за email

user1 = User("John", "john@example.com")
user2 = User("Mike", "john@example.com")
user3 = User("Alice", "alice@example.com")

print(user1 == user2)  # Виведе: True
print(user1 == user3)  # Виведе: False
# __eq__ дозволяє визначити, як порівнюються об'єкти. У нашому випадку — за email.


"""Абстрактні класи""" # Абстрактний клас містить методи, які повинні бути реалізовані в дочірніх класах. Використовується для створення загального інтерфейсу.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Абстрактний метод, обов’язковий для реалізації в підкласах

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog = Dog()
dog.make_sound()  # Виведе: Woof! Woof!

cat = Cat()
cat.make_sound()  # Виведе: Meow!

# animal = Animal()  # Помилка! Не можна створювати екземпляри абстрактного класу
