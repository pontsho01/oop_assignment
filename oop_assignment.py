# Assignment 1: Design Your Own Class! 🏗️

# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand       # Public attribute
        self._model = model      # Protected attribute (convention)
        self.__price = price     # Private attribute (name mangling)

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive!")

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self._model}, Price: ${self.__price}")

# Child class inherits Smartphone
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, price, camera_megapixels):
        super().__init__(brand, model, price)
        self.camera_megapixels = camera_megapixels

    def show_info(self):
        # Polymorphism: Override method to include camera info
        super().show_info()
        print(f"Camera: {self.camera_megapixels} MP")

# Activity 2: Polymorphism Challenge! 🎭

class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Testing the classes

# Assignment 1 test
print("=== Smartphone Classes ===")
phone1 = Smartphone("Samsung", "Galaxy S21", 999)
phone1.show_info()
phone1.set_price(899)
phone1.show_info()

phone2 = SmartphoneWithCamera("Apple", "iPhone 14", 1200, 12)
phone2.show_info()
phone2.set_price(-100)  # Test invalid price

print("\n=== Polymorphism Test ===")
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
