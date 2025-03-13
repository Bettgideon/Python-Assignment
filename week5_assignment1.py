# Parent Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def display_info(self):
        return f"{self.brand} {self.model} costs ${self.price}."

# Child Class: Advanced Smartphone (Inheritance & Encapsulation)
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, price, camera_megapixels, battery_life):
        super().__init__(brand, model, price)
        self.__camera_megapixels = camera_megapixels  # Encapsulation
        self.battery_life = battery_life

    def camera_quality(self):
        return f"{self.brand} {self.model} has a {self.__camera_megapixels}MP camera."

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S21", 799)
phone2 = AdvancedSmartphone("Apple", "iPhone 15 Pro", 1199, 48, "20 hours")

