import random
import string


def safe_to_file(password):
    is_safe = input(f"\nЗберегти пароль - {password} у файл? (+-): ").strip()
    if is_safe == "+":
        with open("password_list.txt", "a") as file:
            file.write(password + "\n")
        print(f"\nПароль - {password}, збережено у файл")
    else:
        print("Пароль не збережено")


def do_random_password(prompt, ask_len_password):
    while True:
        password = "".join(random.choices(prompt, k=ask_len_password))
        is_true = input(f"Ваш пароль - {password}. Він вам підходить?(+-): ")
        if is_true == "+":
            return password


def look_list_password():
    try:
        with open("password_list.txt", "r") as file:
            passwords = [line.strip() for line in file.readlines()]
        if not passwords:
            print("Файл порожній або не знайдено")
            return
        print("\nСписок паролів")
        for i, pasw in enumerate(passwords, 1):
            print(f"{i}. {pasw}")
        return passwords
    except FileNotFoundError:
        print("Файл не знайдено")
        return None


def delete_password():
    passwords = look_list_password()
    if not passwords:
        return
    while True:
        try:
            num = int(input("Введіть номер пароля який ви хочете видалити: "))
            if 1 <= num <= len(passwords):
                break
            else:
                print("Невірний номер, спробуйте ще раз")
        except ValueError:
            print("Введіть число менше 1")
    del passwords[num - 1]
    with open("password_list.txt", "w") as file:
        file.writelines(pw + "\n" for pw in passwords)  # Додаємо переноси рядків
    print("Пароль успішно видалено")


optional = [
    string.digits,
    string.ascii_letters,
    string.digits + string.ascii_letters,
    string.digits + string.ascii_letters + string.punctuation
]


def get_valid_number(prompt_text, min_value):
    while True:
        try:
            value = int(input(prompt_text))
            if value >= min_value:
                return value
            print(f"Введіть число не менше {min_value}")
        except ValueError:
            print(f"Введіть коректне число (мінімальне {min_value})")


while True:
    print("\n\nМеню генератора паролів: ")
    menu_option = [
        "Згенерувати новий пароль",
        "Показати мої збережені паролі",
        "Видалити пароль зі збережених",
        "Вийти з програми"
    ]
    for i, option in enumerate(menu_option, 1):
        print(f"{i}. {option}")
    number_action = get_valid_number("Виберіть опцію(1-4): ", 1)

    if number_action == 1:
        print("\nВиберіть з чого буде складатися ваш пароль:")
        password_option = [
            "Тільки цифри",
            "Тільки букви",
            "Букви + цифри",
            "Символи + букви + цифри",
            "Запропонувати свій набір символів"
        ]
        for i, option in enumerate(password_option, 1):
            print(f"{i}. {option}")
        while True:
            try:
                ask_action = get_valid_number("Виберіть з чого буде складатися ваш пароль(1-5): ", 1)
                if ask_action not in range(1, 6):
                    raise ValueError
                break
            except ValueError:
                print("Введіть число від 1 до 5")
        if 1 <= ask_action <= 4:
            while True:
                try:
                    ask_len_password = get_valid_number("Введіть довжину пароля: ", 1)
                    if ask_len_password < 1:
                        raise ValueError
                    break
                except ValueError:
                    print("Введіть довжину пароля > 0")
            prompt = optional[ask_action - 1]
            password = do_random_password(prompt, ask_len_password)
            safe_to_file(password)
            break

        elif ask_action == 5:
            while True:
                prompt = input("Запропонуйте свій набір символів: ").strip()
                if prompt:
                    break
                print("Набір символів не може бути порожнім")
            while True:
                password = "".join(random.sample(prompt, len(prompt)))
                is_true = input(f"Ваш пароль - {password}. Він вам підходить?(+-): ").strip()
                if is_true == "+":
                    safe_to_file(password)
                    break

    elif number_action == 2:
        look_list_password()

    elif number_action == 3:
        delete_password()

    elif number_action == 4:
        print("Вихід з програми...")
        break
