class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def print_information(self):
        print(f"The name of dish: {self.name}, The price: {self.price}")

class Order:
    def __init__(self):
        self.list_of_dish = []

    def add_dish(self, dish, quantity):
        if quantity > 0:
            self.list_of_dish.append((dish, quantity))
        else:
            print("We dont have this dish in our menu")

    def calculate_total(self):
        total_price = sum(dish.price * quantity for dish, quantity in self.list_of_dish)
        return total_price

    def print_list_and_total(self):
        print("Your order:")
        for dish, quantity in self.list_of_dish:
            print(f"{dish.name} - {quantity}at. - {dish.price * quantity} UAN")
        print(f"Total: {self.calculate_total()} UAN")

burger = Dish("Burger", 100)
coffe = Dish("Coffe", 50)
dessert = Dish("Dessert", 120)

order = Order()
order.add_dish(burger, 2)
order.add_dish(coffe, 1)
order.add_dish(dessert, 1)

order.print_list_and_total()