import os

# Функція для збереження завдань у файл
def safe_to_file():
    if not tasks:  # Якщо список порожній, не зберігаємо
        print("Немає завдань для збереження.")
        return
    if not os.path.exists('image'):
        os.makedirs('image')  # Створюємо папку, якщо її немає
    with open("image/task_list.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(tasks))  # Записуємо список у файл коректно
    print("Завдання збережено у файл")

# Функція для завантаження завдань з файлу
def load_task_from_file():
    try:
        with open("image/task_list.txt", "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        return []

tasks = load_task_from_file()  # Завантажуємо завдання при старті

# Функція для відображення списку завдань
def show_task():
    if not tasks:
        print("Немає завдань у вашому списку")
        return False
    print("\nВаші завдання:")
    for i, task in enumerate(tasks, 1):  # Нумеруємо список коректно
        print(f"{i}. {task}")
    return True

# Функція для перевірки коректного введення чисел
def save_input(prompt, min_val, max_val):
    while True:
        try:
            user_input = int(input(prompt))
            if min_val <= user_input <= max_val:
                return user_input
            else:
                print(f"Введіть число в проміжку від {min_val} до {max_val}")
        except ValueError:
            print("Введіть конкретне число!!!")

# Функція для оновлення та збереження змін у файлі
def update_and_save(index, new_value):
    tasks[index] = new_value
    safe_to_file()

# Головний цикл програми
while True:
    print("\nМеню")
    print("1. Додати завдання.")
    print("2. Переглянути завдання")
    print("3. Видалити завдання")
    print("4. Змінити завдання")
    print("5. Вихід")

    choice = save_input("Введіть число (1-5): ", 1, 5)

    if choice == 1:
        task = input("Напишіть ваше завдання: ").strip()
        if task:
            tasks.append(task)
            safe_to_file()  # Зберігаємо після додавання
            print("Ваше завдання додано")
        else:
            print("Завдання не може бути порожнім!")

    elif choice == 2:
        show_task()

    elif choice == 3:
        if show_task():
            del_task = save_input("Введіть номер завдання, яке хочете видалити: ", 1, len(tasks)) - 1
            delete_task = tasks.pop(del_task)
            safe_to_file()  # Оновлюємо файл після видалення
            print(f"Завдання '{delete_task}' було видалено!")

    elif choice == 4:
        if show_task():
            change_task = save_input("Введіть номер завдання, яке хочете змінити: ", 1, len(tasks)) - 1
            new_task = input("Введіть нове завдання: ").strip()
            if new_task:
                update_and_save(change_task, new_task)  # Оновлюємо і зберігаємо
                print("Ваше завдання змінено")
            else:
                print("Нове завдання не може бути порожнім!")

    elif choice == 5:
        safe_to_file()  # Останнє збереження перед виходом
        print("Вихід із програми...")
        break

