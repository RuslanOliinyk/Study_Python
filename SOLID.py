"""Принцип єдиного обов'язку (Single Responsibility Principle - SRP)"""
class User:
    def __init__(self, name="", lastname="", age=None):
        self.name = name
        self.lastname = lastname
        self.age = age

    # Відповідає за створення користувача
    def create_user(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    # Відповідає за оновлення даних користувача
    def update_user(self, name=None, lastname=None, age=None):
        if name:
            self.name = name
        if lastname:
            self.lastname = lastname
        if age:
            self.age = age

    # Відповідає за видалення користувача
    def delete_user(self):
        self.name = None
        self.lastname = None
        self.age = None











#---------------------------------------------------------------------------------------

"""Принцип відкритості/закритості (Open/Closed Principle - OCP)"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()









#---------------------------------------------------------------------

""" Принцип підстановки Лісков (Liskov Substitution Principle - LSP)"""

""" Ми забезпечили принцип підстановки Лісков (LSP), оскільки об'єкти
підкласів (Circle) і (Square) можуть бути використані замість базового
класу (Shape) без порушення функціональності. Код залишається гнучким, 
і ви можете додавати нові фігури (наприклад, трикутники, прямокутники),
які будуть коректно працювати з тією ж самою функціональністю."""


from abc import ABC, abstractmethod
import math

# Базовий клас Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Підклас Circle (Коло)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Підклас Square (Квадрат)
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

# Тестування
def print_shape_info(shape: Shape):
    print(f"Площа: {shape.area()}")
    print(f"Периметр: {shape.perimeter()}")

# Використання
circle = Circle(5)
square = Square(4)

print("Інформація про коло:")
print_shape_info(circle)

print("\nІнформація про квадрат:")
print_shape_info(square)





#---------------------------------------------------------

"""Принцип інтерфейсу користувача (Interface Segregation Principle - ISP)"""

"""Принцип сегрегації інтерфейсу (Interface Segregation Principle - ISP)
полягає в тому, що не слід примушувати класи реалізовувати методи, які 
вони не використовують. Це означає, що якщо є інтерфейс, який має багато
методів, то краще розділити його на декілька менших інтерфейсів, кожен 
з яких відповідає тільки за одну конкретну задачу."""


from abc import ABC, abstractmethod

# Інтерфейс для друку
class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

# Інтерфейс для сканування
class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

# Інтерфейс для копіювання
class Copier(ABC):
    @abstractmethod
    def copy_document(self):
        pass

# Клас Printer реалізує тільки Printer
class PrinterDevice(Printer):
    def print_document(self, document):
        print(f"Друкується документ: {document}")

# Клас Scanner реалізує тільки Scanner
class ScannerDevice(Scanner):
    def scan_document(self):
        print("Сканування документа...")

# Клас MultiFunctionPrinter реалізує всі три інтерфейси
class MultiFunctionPrinter(Printer, Scanner, Copier):
    def print_document(self, document):
        print(f"Многофункціональний принтер друкує документ: {document}")

    def scan_document(self):
        print("Многофункціональний принтер сканує документ...")

    def copy_document(self):
        print("Многофункціональний принтер копіює документ...")

# Приклад використання
printer = PrinterDevice()
printer.print_document("Звіт")

scanner = ScannerDevice()
scanner.scan_document()

multi_function_printer = MultiFunctionPrinter()
multi_function_printer.print_document("Інструкція")
multi_function_printer.scan_document()
multi_function_printer.copy_document()










#-------------------------------------------------------------------
"""Принцип залежностей (Dependency Inversion Principle - DIP)"""

"""Принцип інверсії залежностей (Dependency Inversion Principle - DIP)
полягає в тому, що високорівневі модулі не повинні залежати від низькорівневих,
а обидва повинні залежати від абстракцій. Абстракції не повинні залежати від 
деталей, а деталі повинні залежати від абстракцій. В результаті цього ми можемо
зробити код більш гнучким, масштабованим і легким для тестування."""

from abc import ABC, abstractmethod

# Абстракція принтера
class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

# Конкретна реалізація принтера
class LaserPrinter(Printer):
    def print_document(self, document):
        print(f"Лазерний принтер друкує документ: {document}")

class InkjetPrinter(Printer):
    def print_document(self, document):
        print(f"Принтер струйний друкує документ: {document}")

# Клас для генерації звітів, який використовує абстракцію Printer
class ReportGenerator:
    def __init__(self, printer: Printer):
        self.printer = printer

    def generate_report(self, content):
        document = f"Звіт: {content}"
        self.printer.print_document(document)

# Створюємо об'єкти конкретних принтерів
laser_printer = LaserPrinter()
inkjet_printer = InkjetPrinter()

# Тепер клас ReportGenerator не залежить від конкретного принтера
report_generator_laser = ReportGenerator(laser_printer)
report_generator_inkjet = ReportGenerator(inkjet_printer)

# Генерація звітів з різними принтерами
report_generator_laser.generate_report("Фінансова звітність")
report_generator_inkjet.generate_report("Аналіз продажів")
