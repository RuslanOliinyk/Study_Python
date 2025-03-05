import math
print(math.sqrt(16))  # Використовуємо функцію sqrt з модуля math

from math import sqrt
print(sqrt(16))  # Без "math." перед sqrt

import math as m
print(m.sqrt(16))  # Використовуємо псевдонім "m" замість "math"

# my_module.py
def greet(name):
    print(f"Hello, {name}!")

import my_module
my_module.greet("Alice")
