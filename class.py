class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.inf(name, species, age)
        self.make_sound(name, species)

    def inf(self):
        print(f"{self.name}, {self.species}, {self.age}")

    def make_sound(self, name, species):
        if species == "dog":
            print("WOOF")
        elif species == "cat":
            print("MIAUUUUU")
        elif species == "cow":
            print("MUUUUUU")
        else:
            print(f"{name} makes an unknown sound.")

cat = Animal("Tom", "cat", 3)
dog = Animal("Barsik", "dog", 5)
cow = Animal("Marina", "cow", 7)


-----------------------------------------------------------------------------------



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.calculate_area()
    def calculate_area(self):
        if self.width == 0 and self.height == 0:
            print("Error")
        else:
            print(f"{self.width} * {self.height} = {self.width * self.height}")

Rectangle1 = Rectangle(2, 3)
Rectangle2 = Rectangle(4, 3)

-----------------------------------------------------------------------------------

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        return area

# Створення двох об'єктів класу Rectangle
rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(7, 3)

# Виклик методів для обчислення площі
area1 = rectangle1.calculate_area()
area2 = rectangle2.calculate_area()

# Виведення площі на екран
print(f"The area of the first rectangle is: {area1}")
print(f"The area of the second rectangle is: {area2}")

-----------------------------------------------------------

class Vehicle:
    """It's a base class for a Vehicle"""
    def __init__(self, tipe, color) -> None:
        self.tipe = tipe
        self.color = color

    def move(self):
        print("Your vehucle is moving")

class Car(Vehicle):
    """Class Car"""
    def __init__(self,type, color, cost=0) -> None:
        super().__init__(type, color)
        self.cost = cost

    def move(self):
        print(f"{self.color}, {self.tipe} is driving")
        print(f"Cost of this car: {self.cost}")

class Bicycle(Vehicle):
    """Class Bicycle"""
    def __init__(self, type, color, count_of_weels):
        super().__init__(type, color)
        self.count_of_weels = count_of_weels

    def move(self):
        print(f"{self.tipe}, {self.color} is jump")
        print(f"The coun of weels: {self.count_of_weels}")

car1 = Car("sedan", "black", 12000)
car1.move()

bicycle1 = Bicycle("MTB", "Grey", 27.5)
bicycle1.move()


------------------------------------------------------------------------------

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def print_car(self):
        print(f"Maker: {self.make}, Model: {self.model}, Model year: {self.year}, Type of fuel: {self.fuel_type}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type, radius_of_weel):
        super().__init__(make, model, year)
        self.type = type
        self.radius_of_weel = radius_of_weel

    def print_moto(self):
        print(f"Maker: {self.make}, Model: {self.model}, Model year: {self.year}, Class of moto: {self.type}, Padius of wheel: {self.radius_of_weel}")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

    def print_bike(self):
        print(f"Maker: {self.make}, Model: {self.model}, Model year: {self.year}, Class of bicycle: {self.type}")

car1 = Car("BMW", "M5", 2008, "Gasoline")
moto1 = Motorcycle("KTM", "EXC", 2025, "Enduro", 21)
bicycle1 = Bicycle("Zoom", "g45", 2018, "MTB")

car1.print_car()
moto1.print_moto()
bicycle1.print_bike()

--------------------------------------------------------------------

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Maker: {self.make}, Model: {self.model}, Model year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Maker: {self.make}, Model: {self.model}, Model year: {self.year}, Type of fuel: {self.fuel_type}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type, radius_of_weel):
        super().__init__(make, model, year)
        self.type = type
        self.radius_of_weel = radius_of_weel

    def display_info(self):
        print(f"Maker: {self.make}, Model: {self.model}, Model year: {self.year}, Class of moto: {self.type}, Padius of wheel: {self.radius_of_weel}")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

    def display_info(self):
        print(f"Maker: {self.make}, Model: {self.model}, Model year: {self.year}, Class of bicycle: {self.type}")

car1 = Car("BMW", "M5", 2008, "Gasoline")
moto1 = Motorcycle("KTM", "EXC", 2025, "Enduro", 21)
bicycle1 = Bicycle("Zoom", "g45", 2018, "MTB")

car1.display_info()
moto1.display_info()
bicycle1.display_info()

---------------------------------------------------------------------------------

class Counter:
    """Count of something"""
    def __init__(self, count_obj, type_obj, max_elements) -> None:
        self.count_obj = count_obj
        self.type_obj = type_obj
        self.max_elements = max_elements
    def counter(self):
        print(f"Type of object: {self.type_obj}")
        if isinstance(self.count_obj, (list, dict, str, tuple)):
            count = len(self.count_obj)
            if count > self.max_elements:
                print("Count elements of your object more than need")
                print(f"More on {count - self.max_elements}")
            else:
                print(f"Count of elements: {count}")

        else:
            print("Your object must be iterable")

    def get_attr(self):
        print(self.__dict__)

    def set_attr(self, attr, value):
        if hasattr(self, self.__dict__[attr]):
            setattr(self, self.__dict__[attr], value)
        else:
            print("Check your attrs")

class ListElenents(Counter):
    """Class for list elements"""
    def __init__(self, count_obj, type_obj, max_elements) -> None:
        super().__init__(count_obj, type_obj, max_elements)
        pass

    def counter(self):
        super().counter()

        print("Operation was ended")

list_ex = ListElenents([1, 2, 3, 4], list, 10)
list_ex.counter()

----------------------------------------------------------------

class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name



    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def print_user(self):
        print(f"Name: {self.__name}, Email: {self.__email}, Password: {self.__password}")

user1 = User("Mykola", "hlopzsela@gmail.com", "1111")
user1.print_user()
user1.set_name("Tom")
user1.print_user()

print(user1.get_name())
print(user1.get_email())
print(user1.get_password())


-------------------------------------------------------------------------------------------------------


from abc import ABC, abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def calculate_area(self):
        pass

    @abstractclassmethod
    def print_result(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.area_circle = None

    def calculate_area(self):
        self.area_circle = 3.14 * (self.radius ** 2)

    def print_result(self):
        print(f"Area of circle: {self.area_circle}")


class Rectangle(Shape):
    def __init__(self, hight, width):
        self.hight = hight
        self.width = width
        self.area_rectangle = None

    def calculate_area(self):
        self.area_rectangle = self.hight * self.width

    def print_result(self):
        print(f"Area of rectangle: {self.area_rectangle}")


class Triangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.area_triangle = None

    def calculate_area(self):
        self.area_triangle = 0.5 * self.a * self.b

    def print_result(self):
        print(f"Area of triangle: {self.area_triangle}")


circle1 = Circle(5)
circle1.calculate_area()
circle1.print_result()

rectangle1 = Rectangle(3, 8)
rectangle1.calculate_area()
rectangle1.print_result()

triangle1 = Triangle(4, 6)
triangle1.calculate_area()
triangle1.print_result()


----------------------------------------------------------------------

class User:
    def __init__(self, name, gmail):
        self.name = name
        self.gmail = gmail

    def greet(self):
        print(f"Hello {self.name}")

class Admin(User):
    def ban_user(self, user):
        print(f"User {user.name} has been banned!")

# Приклад використання
user1 = User("John", "john@example.com")
admin1 = Admin("Alice", "alice@example.com")

user1.greet()  # Виведе: Hello John
admin1.ban_user(user1)  # Виведе: User John has been banned!



---------------------------------------------------------------


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def print_result(self):
        pass

    def __str__(self):
        return f"Shape: {self.__class__.__name__}"

    def compare_area(self, other):
        """Порівнює площу поточного об'єкта з іншою фігурою"""
        if not isinstance(other, Shape):
            raise TypeError("Можна порівнювати тільки об'єкти класу Shape")

        if self.area() > other.area():
            print(f"{self} has a larger area than {other}")
        elif self.area() < other.area():
            print(f"{other} has a larger area than {self}")
        else:
            print(f"{self} and {other} have the same area")

    def scale(self, factor):
        """Змінює розмір фігури у `factor` разів"""
        raise NotImplementedError("Метод scale() повинен бути реалізований у підкласах")

class Rectangle(Shape):
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def area(self):
        return self.h * self.w

    def print_result(self):
        print(f"The area of the rectangle ({self.h} × {self.w}) = {self.area()}")

    def scale(self, factor):
        self.h *= factor
        self.w *= factor

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return round(3.14 * (self.r ** 2), 2)

    def print_result(self):
        print(f"The area of the circle (radius {self.r}) = {self.area():.2f}")

    def scale(self, factor):
        self.r *= factor

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def print_result(self):
        print(f"The area of the triangle (base {self.base}, height {self.height}) = {self.area()}")

    def scale(self, factor):
        self.base *= factor
        self.height *= factor

# Список фігур
shapes = [
    Rectangle(5, 26),
    Rectangle(8, 6),
    Circle(5),
    Circle(3),
    Triangle(10, 5),
    Triangle(6, 8)
]

# Вивід результатів
for shape in shapes:
    print(shape)
    shape.print_result()
    print("-" * 30)

# Порівняння площ
shapes[0].compare_area(shapes[1])  # Порівнюємо два прямокутники
shapes[2].compare_area(shapes[3])  # Порівнюємо два кола

# Масштабування однієї з фігур
print("\nScaling the first rectangle by a factor of 2...")
shapes[0].scale(2)
shapes[0].print_result()
