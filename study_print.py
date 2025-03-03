print("Hello \nWorld") # \n - Перехід на новий рядок
print("Hello \tWorld") # \t - Табуляція в 4 пробіли
print("Hello \\World") # \\ - Ставить зворотній слеш
print("Hello 'World'") # Одинарні лапки якщо спочатку ставились подвійні
print("Hello \'World\' ") # \' \' - Напис одинарних лапок
print("Hello \"World\" ") # \" \" - напис подвійних лапок


print("Apple", "Banana", "Cherry", sep=", ") #sep="" розділювальний знак

print("Hello", end=" --- ") #end="" те що ми ставимо в кінці рядка без переходу на інший
print("World")

with open("", "w") as f:
    print("Hello world", file=f) # Вивід у файлі

print("1", "2", "3", "4", "5", sep="-")
print("Hello \nHow are you? \nHave a nace day!")
print("Python\tis\tawesome")
print("Hello", end=" ")
print("World")
print("This is \"Python\"")

print("Hello\b!") # \b - Видаляє останній символ
print("Hallo World\rBye") # \r - Видаляє все що є перед ним і виводить тільки те що після нього
print("\a") # \a - Видає звук

import sys
sys.stdout.write("Hallo World") # - За замовчуванням не додає \n в кінці, зручно коли треба зробити програму в які не потрібно переходити на новий рядок

print(False and True) # Виведе False
print(True and True) # Виведе True


import time

text = ("Loading...")
for i in text:
    sys.stdout.write(i)
    sys.stdout.flush() # Оновлює екран без затримки
    time.sleep(0.3)

text = ("Loading...")
for i in text:
    print(i, end="", flush=True)
    time.sleep(0.3)


for i in range(5, 0, -1):
    print(f"\rЗалишилось {i} секунд", end="", flush=True) # flush= - Оновлює екран без затримки
    time.sleep(1) # Виводить з затримкою в часі
print("\rЧас вийшов!")