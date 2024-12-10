# Parent class
class Vehicle:
    def move(self):
        return "This vehicle moves."

# Child classes with polymorphism
class Car(Vehicle):
    def move(self):
        return "Driving 🚗."

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️."

class Boat(Vehicle):
    def move(self):
        return "Sailing 🛥️."

# Example usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
