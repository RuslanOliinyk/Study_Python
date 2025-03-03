"""Спискове включення(List Comprehension)"""
squares = [x**2 for x in range(0, 11)] # [] - Використовується для створення списку на основі іншого списку або послідовності
print(squares)

even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)

"""Генератор множин. Set Comprehension"""
unique = {x**2 for x in [1, 2, 3, 3, 4, 4, 5]} # {} - створює множину без дублікатів
print(unique)


"""Генератор словників. Dictionary Comprehension"""
unique = {x: x**2 for x in [1, 2, 3, 3, 4, 4, 5]} # {} - створює словник
print(unique)


"""Генератори (Замість списків). Не створює список а генерує значення по одному"""

gen = (x**2 for x in range(5)) # Економить пам'ять тим що не створює одразу весь список, а генерує значення по одному. Для виводу наступного потрібно змінну обернути в - next()
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 4
print(next(gen)) # 9


"""Вкладені цикли в рядок""" # Якщо треба перебрати два списки(або вкладений список), можна використовувати подвійний for
products = [x * y for x in range(1, 4) for y in range(1, 4)] # Перемноження всіх комбінацій двох списків.
print(products)




-------------------------------------------------------------------------------


for i in range(10, 0, -1):
    print(i)

----------------------------------------

num = int(input("Enter number: "))
for i in range(1, num + 1):
    print(f"{num} * {i} = {num * i}")

----------------------------------------

for i in range(1, 31):
    if i % 2 == 0:
        print(i)

----------------------------------------

num = input("Enter your number: ")
lot = 0
for i in num:
    if int(i) % 2 == 0:
        lot += 1
print(f"Number of even digits: {lot}")

----------------------------------------

num = int(input("Enter your number: "))
original = num
reserved_num = 0

while num > 0:
    digit = num % 10
    reserved_num = reserved_num * 10 + digit
    num //= 10

if original == reserved_num:
    print("This palindrom")
else:
    print("This not palindrom")

-------------------------------------------

num = int(input("Enter your number: "))
max_num = 0

while num > 0:
    digit = num % 10
    if digit > max_num:
        max_num = digit
    num //= 10

print(f"Max digits: {max_num}")

----------------------------------------------


def sum_fibonachi(limit):
    a, b = 0, 1
    total = 0
    while a <= limit:
        total += a
        a, b = b, a + b
    return total


limit = int(input("Enter your limit: "))
result = sum_fibonachi(limit)
print(f"Sum digit fibonachi: {result}")

----------------------------------------------------

weight = int(input("Enter weight: "))
heigt = int(input("Enter height: "))
symvol = "# "
a = 0
while a <= heigt:
    print(weight * symvol)
    a += 1

# Другий спосіб

weight = int(input("Enter weight: "))
heigt = int(input("Enter height: "))
symvol = "# "
for _ in range(heigt):
    print(symvol * weight)

---------------------------------------------------

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}", end="    \t", )
    print()

------------------------------------------------------

n = int(input("Enter number: "))

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()

---------------------------------------------------------

import random

num_comp = random.randint(1, 100)
num_user = 0
while num_user != num_comp:
    num_user = int(input("Enter number: "))
    if num_user == num_comp:
        print("You win!!!")
    elif num_user < num_comp:
        print("Your number is too low")
    else:
        print("Your number is too high")


-------------------------------------------------------------


number = [1, 2, 2, 3, 4, 4, 5]

def unique_numbers(number):
    unique_list = []
    for i in number:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

output_list = unique_numbers(number)
print(output_list)

---------------------------------------------------------------------

"""НСД"""
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
longer = max(num1, num2)
the_bigest_num = 0
for i in range(1, longer + 1):
    if num1 % i == 0 and num2 % i == 0:
        the_bigest_num = i
print(the_bigest_num)

------------------------------


"""Другий спосіб. Алгоритм Евкліда"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

the_bigest_num = gcd(num1, num2)

print("The greatest common divisor is:", the_bigest_num)