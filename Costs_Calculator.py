from datetime import datetime
from collections import defaultdict


def get_valid_number(text, min_value, max_value):
    try:
        value = int(input(text))
        if max_value >= value >= min_value:
            return value
        print(f"Число повинно бути від {min_value} до {max_value}")
    except ValueError:
        print(f"Введіть число від {min_value} до {max_value}")


def add_costs(user_info):
    try:
        with open("expenses.txt", "a") as file:
            user_info[0] = f"{user_info[0]:.2f}"
            safe_cost = ", ".join(map(str, user_info))
            file.writelines(safe_cost + "\n")
            print(f"Витрату \"{safe_cost}\" збережено у файл")

    except FileNotFoundError:
        print("Файл не знайдено")


def load_cost():
    try:
        with open("expenses.txt", "r") as file:
            all_costs = [line.strip() for line in file.readlines()]
        if not all_costs:
            print("Ваш список витрат порожній")
            return []
        for i, line in enumerate(all_costs, 1):
            print(f"{i}. {line}")
        return all_costs
    except FileNotFoundError:
        print("Файл порожній або його не знайдено")
        return []


def delete_costs():
    costs = load_cost()
    if not costs:
        return
    while True:
        try:
            num = int(input("Введіть номер витрати яке ви хочете видалити: "))
            if 1 <= num <= len(costs):
                break
            else:
                print("Номер поза межами списку!")
        except ValueError:
            print("Введіть число")
    del costs[num - 1]

    with open("expenses.txt", "w") as file:
        file.writelines((cs + "\n" for cs in costs))
    print("Витрату успішно видалено")


def sum_all_costs():
    costs = load_cost()
    if not costs:
        return

    total = 0

    for line in costs:
        parts = line.split(", ")
        try:
            total += float(parts[0])
        except ValueError:
            print(f"Помилка в записі: {line}")
    print(f"Загальна сума витрат становить: {total:.2f} $")


def load_sort_costs():
    try:
        with open("expenses.txt", "r") as file:
            all_costs = [line.strip() for line in file.readlines()]
        if not all_costs:
            print("Ваш список витрат порожній")
            return []
        costs_by_category = defaultdict(list)
        for line in all_costs:
            parts = line.split(", ")
            if len(parts) < 3:
                print(f"Некоректний запис: {line}")
                continue
            cost, category, date = parts
            costs_by_category[category].append(f"{cost} $ ({date})")
        sorted_categories = sorted(costs_by_category.keys())

        print("\n**Витрати за категоріями:**")

        for category in sorted_categories:
            print(f"\n {category}:")
            for item in costs_by_category[category]:
                print(f"   - {item}")
    except FileNotFoundError:
        print("Файл порожній або його не знайдено")
        return []


while True:
    print("\n\nМеню калькулятора витрат:")
    menu_option = [
        "Додати витрати",
        "Переглянути список витрат",
        "Переглянути витрати за категоріями",
        "Видалити витрати",
        "Загальна сума витрат",
        "Вийти з програми"
    ]
    for i, option in enumerate(menu_option, 1):
        print(f"{i}. {option}")

    ask_option = get_valid_number("Оберіть опцію: ", 1, 6)

    if ask_option == 1:
        while True:
            try:
                user_cost = float(input("Введіть вартість витрати: "))
                break
            except ValueError:
                print("Введіть числове значення суми витрати($)")

        user_main = str(input("Введіть категорію витрати: "))

        while True:
            str_date = input("Введіть дату в форматі РРРР-ДД-ММ: ")
            try:
                user_date = datetime.strptime(str_date, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Невірний формат! Спробуйте ще раз.")
        user_info = [user_cost, user_main, user_date]
        add_costs(user_info)

    elif ask_option == 2:
        load_cost()

    elif ask_option == 3:
        load_sort_costs()

    elif ask_option == 4:
        delete_costs()

    elif ask_option == 5:
        sum_all_costs()

    elif ask_option == 6:
        print("Вихід з програми...")
        break
