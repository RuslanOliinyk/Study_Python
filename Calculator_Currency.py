# Список доступних валют
valid_currencies = ["USD", "EUR", "UAH"]

def get_valid_currency(prompt):
    """Функція для введення правильної валюти."""
    while True:
        try:
            valut = input(prompt).upper()
            if valut in valid_currencies:
                return valut
            else:
                print(f"Оберіть одне з значень: {', '.join(valid_currencies)}!!!")
        except ValueError:
            print("Неправильний формат")

def get_valid_amount(prompt):
    """Функція для введення правильної кількості валюти."""
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
            else:
                print("Значення повинно бути > 0")
        except ValueError:
            print("Введіть числове значення!!!")

# Отримуємо введені дані
lot_valut = get_valid_amount("Введіть кількість яку ви хочете конвертувати: ")
from_valut = get_valid_currency("Оберіть валюту з якої ви хочете конвертувати: ")

while True:
    to_valut = get_valid_currency("Оберіть валюту в яку ви хочете конвертувати: ")
    if from_valut == to_valut:
        print(f"Не можна переводити {from_valut} в {to_valut}, виберіть іншу валюту.")
    else:
        break

# Курси валют
exchange_rates = {"USD": 1, "EUR": 0.92, "UAH": 38.5}

def calculate_valut(num, first, second):
    """Функція для конвертації валюти."""
    usd_mount = num / exchange_rates[first]
    result = usd_mount * exchange_rates[second]
    return result

# Розрахунок і вивід результату
change_valut = calculate_valut(lot_valut, from_valut, to_valut)
print(f"{lot_valut} {from_valut} = {change_valut:.2f} {to_valut}")
