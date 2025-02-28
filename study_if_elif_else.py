"""Перевірка числа на парність"""
number = int(input("Enter your number: "))

if number % 2 == 0:
    print("Your number is couple")
else:
    print("Your number is not couple")

#Другий варіант

print("Your number is couple" if int(input("Enter your number:")) % 2 == 0 else "Your number is not couple")

--------------------------------------------------

"""Перевірка числа чи воно більше, менше, рівне 0"""

number = float(input("Enter your number: "))

if number > 0:
    print("Your number > 0")
elif number == 0:
    print("Your number = 0")
else:
    print("Your number < 0")

#Другий варіант

number = float(input("Enter your number: "))

print("Your number > 0" if number > 0 else "Your number = 0" if number == 0  else "Your number < 0")


--------------------------------------------------

"""Порівняння двох чисел та узгодження типів даних"""

num_1 = input("Enter your first number: ")
num_2 = input("Enter your second number: ")

num_1 = float(num_1)
num_2 = float(num_2)

if num_1.is_integer():
    num_1 = int(num_1)
if num_2.is_integer():
    num_2 = int(num_2)

if num_1 > num_2:
    print(f"{num_1} > {num_2}")
elif num_1 == num_2:
    print(f"{num_1} = {num_2}")
else:
    print(f"{num_1} < {num_2}")


----------------------------------------------------------

"""Переведення оцінки студента"""

mark = int(input("Введіть вашу оцінку за шкалою 0-100: "))

if 90 <= mark <= 100:
    print("Відмінно")
elif 70 <= mark <= 89:
    print("Добре")
elif 50 <= mark <= 69:
    print("Задовільно")
elif 0 <= mark <= 49:
    print("Не склав")

else:
    print("Ви невірно ввели вашу оцінку")


------------------------------------------------------------------

"""Перевірка чи є рік високосним"""

year = int(input("Введіть рік: "))

if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
    print("Ваш рік високосний")
else:
    print("Ваш рік не високосний")


-------------------------------------------------------------------


"""Калькулятор з двома числами та перевіркою типу даних результатів"""

num_1 = input("Enter your first number: ")
action = str(input("Chose your action(+,-,/,*): "))
num_2 = input("Enter your second number: ")

num_1 = float(num_1)
num_2 = float(num_2)

if num_1.is_integer():
    num_1 = int(num_1)
if num_2.is_integer():
    num_2 = int(num_2)

def isInt(result):
    if result.is_integer():
        return int(result)
    return result

if action == "+":
    result = num_1 + num_2
    print(f"Result {num_1} + {num_2} = {isInt(result)}")
elif action == "-":
    result = num_1 - num_2
    print(f"Result {num_1} - {num_2} = {isInt(result)}")
elif action == "/":
    if num_2 != 0:
        result = num_1 / num_2
        print(f"Result {num_1} / {num_2} = {isInt(result)}")
    else:
        print("Cannot be divided by zero")

elif action == "*":
    result = num_1 * num_2
    print(f"Result {num_1} * {num_2} = {isInt(result)}")
else:
    print("You enter false action")


----------------------------------------------------------


"""Перевірка чи трикутник існує"""

side_1 = input("Enter fist side: ")
side_2 = input("Enter second side: ")
side_3 = input("Enter third side: ")

side_1 = float(side_1)
side_2 = float(side_2)
side_3 = float(side_3)

if side_1.is_integer():
    side_1 = int(side_1)
if side_2.is_integer():
    side_2 = int(side_2)
if side_3.is_integer():
    side_3 = int(side_3)

if (side_1 + side_2) > side_3 and (side_1 + side_3) > side_2 and (side_2 + side_3) > side_1:
    print(f"The triagle exists: {side_1} + {side_2} > {side_3}, {side_1} + {side_3} > {side_2}, {side_2} + {side_3} > {side_1}")
else:
    print("The triagle not exists")


--------------------------------------------------------------------------

"""Авторизація за логіном та паролем"""

log = input("Enter login: ")
pasw = input("Enter your password: ")

login = "admin"
password = "1234"

if log == login and pasw == password:
    print("You input in system")
elif log != login and pasw == password:
    print("Login is wrong")
elif log == login and pasw != password:
    print("Password is wrong")
else:
    print("Login and password is wrong")


-----------------------------------------------------------

"""Переведення 24 годинного формату в 12"""


hour = int(input("Enter hour(0-23): "))
minutes = int(input("Enter minutes(0-59): "))

if 0 <= hour <= 11 and 0 <= minutes <= 59:
    period = "AM"
    display_hour = 12 if hour == 0 else hour
elif 12 <= hour <= 23 and 0 <= minutes <= 59:
    period = "PM"
    display_hour = 12 if hour == 12 else hour - 12
else:
    print("You enter wrong hour or minutes")
print(f"{display_hour}:{minutes:02d} {period}")


------------------------------------------------------------

"""Гра з камінь, ножиці, папір з компютером"""

import random
user = input("Виберіть дію(Камінь, Ножиці, Папір): ").lower()

comp = ["Камінь", "Ножиці", "Папір"]
random_comp = random.choice(comp)

print(f"You: {user.capitalize()} - computer: {random_comp.capitalize()}")

if user == random_comp:
    print("Нічия")
elif (user == "Камінь" and random_comp == "Ножиці") or \
     (user == "Ножиці" and random_comp == "Папір") or \
     (user == "Папір" and random_comp == "Камінь"):
    print("Ви виграли")
elif (user == "Камінь" and random_comp == "Папір") or \
     (user == "Ножиці" and random_comp == "Камінь") or \
     (user == "Папір" and random_comp == "Ножиці"):
    print("Ви програли")
else:
    print("You entered wrong action")

