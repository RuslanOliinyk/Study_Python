class Book:

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"Назва книги: {self.title}, Автор: {self.author}, Жанр: {self.genre}"

class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' додана в бібліотеку.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Книга '{title}' видалена.")
                return
        print(f"Книгу '{title}' не знайдено в бібліотеці.")

    def list_books(self):
        if self.books:
            print("\nСписок доступних книг:")
            for book in self.books:
                print(book)
        else:
            print("Список книг порожній")

    def search_by_author(self, author):
        found_books = [book for book in self.books if book.author == author]
        if found_books:
            print(f"\nКниги автора '{author}':")
            for book in found_books:
                print(book)
        else:
            print(f"Книгу з автором '{author}' не знайдено в бібліотеці.")

    def search_by_genre(self, genre):
        found_books = [book for book in self.books if book.genre == genre]
        if found_books:
            print(f"\nКниги жанру '{genre}':")
            for book in found_books:
                print(book)
        else:
            print(f"Книгу з жанром '{genre}' не знайдено в бібліотеці.")


# Створення об'єктів книг
book1 = Book("1984", "Джордж Орвелл", "Дистопія")
book2 = Book("Майстер і Маргарита", "Михайло Булгаков", "Фентезі")
book3 = Book("Старий і море", "Ернест Хемінгуей", "Драма")

# Створення об'єкта бібліотеки
library = Library()

# Додавання книг до бібліотеки
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Перегляд всіх книг
library.list_books()

# Пошук книг за автором
library.search_by_author("Михайло Булгаков")

# Пошук книг за жанром
library.search_by_genre("Дистопія")

# Видалення книги
library.remove_book("1984")

