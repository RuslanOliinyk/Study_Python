import json
import os


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class ContactManager:
    FILE_NAME = "contact_list.json"

    def __init__(self):
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r", encoding="utf-8") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []

    def save_contacts(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(self.contacts, file, indent=4, ensure_ascii=False)

    def add_contact(self, contact):
        self.contacts.append(contact.to_dict())
        self.save_contacts()
        print("✅ Контакт успішно збережено!")

    def show_contacts(self):
        if not self.contacts:
            print("❌ В вашому списку немає контактів")
            return None

        print("\n📜 Список контактів:")
        for i, cont in enumerate(self.contacts, 1):
            print(f"{i}. {cont['name']} - {cont['phone']} - {cont['email']}")
        return self.contacts

    def search_by_name(self, name):
        found = [c for c in self.contacts if name.lower() in c["name"].lower()]
        self.print_search_results(found, "ім'ям", name)

    def search_by_phone(self, phone):
        found = [c for c in self.contacts if phone in c["phone"]]
        self.print_search_results(found, "номером", phone)

    def print_search_results(self, results, search_type, value):
        if results:
            print(f"\n🔍 Знайдені контакти за {search_type} {value}:")
            for cont in results:
                print(f"{cont['name']} - {cont['phone']} - {cont['email']}")
        else:
            print(f"❌ Не знайдено жодного контакта з {search_type} {value}")

    def change_contact(self, num, new_contact):
        if 1 <= num <= len(self.contacts):
            self.contacts[num - 1] = new_contact.to_dict()
            self.save_contacts()
            print("✅ Контакт оновлено!")
        else:
            print("❌ Контакт з таким номером не існує!")

    def delete_contact(self, num):
        if 1 <= num <= len(self.contacts):
            deleted_contact = self.contacts.pop(num - 1)
            self.save_contacts()
            print(f"🗑️ Контакт \"{deleted_contact['name']}\" успішно видалено!")
        else:
            print("❌ Контакт з таким номером не існує!")


def get_valid_number(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"❗ Введіть число від {min_value} до {max_value}")
        except ValueError:
            print("❗ Введіть коректне число!")


manager_contact = ContactManager()

while True:
    print("\n📞 Менеджер контактів")
    list_option = [
        "Додати новий контакт",
        "Переглянути список контактів",
        "Шукати контакт",
        "Змінити контакт",
        "Видалити контакт",
        "Вийти з програми"
    ]

    for i, option in enumerate(list_option, 1):
        print(f"{i}. {option}")

    ask_action = get_valid_number("\nОберіть опцію (1-6): ", 1, 6)

    if ask_action == 1:
        name = input("Введіть ім'я: ")
        while True:
            phone = input("Введіть номер телефону: +38 ")
            if phone.startswith("0") and len(phone) == 10:
                break
            else:
                print("❗ Введіть останні 10 цифр телефону!")

        email = input("Введіть Email адрес: ")

        contact = Contact(name, phone, email)
        manager_contact.add_contact(contact)

    elif ask_action == 2:
        manager_contact.show_contacts()

    elif ask_action == 3:
        print("1. Шукати за ім'ям")
        print("2. Шукати за номером телефону")
        ask_search = get_valid_number("Оберіть спосіб пошуку (1,2): ", 1, 2)

        if ask_search == 1:
            search_name = input("Введіть ім'я контакту для пошуку: ")
            manager_contact.search_by_name(search_name)
        else:
            search_phone = input("Введіть номер телефону для пошуку: ")
            manager_contact.search_by_phone(search_phone)

    elif ask_action == 4:
        contacts = manager_contact.show_contacts()
        if contacts:
            num = get_valid_number("\nВведіть номер контакта який ви хочете змінити: ", 1, len(contacts))

            change_name = input("Введіть нове ім'я: ")
            while True:
                change_phone = input("Введіть новий номер телефону: +38 ")
                if change_phone.startswith("0") and len(change_phone) == 10:
                    break
                else:
                    print("❗ Введіть останні 10 цифр телефону!")

            change_email = input("Введіть новий Email адрес: ")

            new_contact = Contact(change_name, change_phone, change_email)
            manager_contact.change_contact(num, new_contact)

    elif ask_action == 5:
        contacts = manager_contact.show_contacts()
        if contacts:
            num = get_valid_number("\nВведіть номер контакта який ви хочете видалити: ", 1, len(contacts))
            manager_contact.delete_contact(num)

    elif ask_action == 6:
        print("👋 Вихід з програми...")
        break
