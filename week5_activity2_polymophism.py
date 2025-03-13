# Parent Class: Vehicle
class Vehicle:
    def move(self):
        pass  # Placeholder for polymorphism

# Child Classes
class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road!"

class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky!"

class Boat(Vehicle):
    def move(self):
        return "🚢 Sailing on the water!"

# Creating objects
car = Car()
plane = Plane()
boat = Boat()

# Printing outputs
print(car.move())   # 🚗 "Driving on the road!"
print(plane.move())  # ✈️ "Flying in the sky!"
print(boat.move())   # 🚢 "Sailing on the water!"
