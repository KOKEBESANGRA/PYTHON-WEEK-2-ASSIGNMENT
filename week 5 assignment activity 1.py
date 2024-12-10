# Parent class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  # Private attribute

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive!")

    def call(self, number):
        return f"Calling {number} from {self.model}."

    def __str__(self):
        return f"{self.brand} {self.model} costs ${self.get_price()}."

# Child class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)
        self.gpu = gpu

    def play_game(self, game):
        return f"Playing {game} with {self.gpu} GPU on {self.model}!"

# Example usage
phone = Smartphone("Apple", "iPhone 15", 999)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 1199, "Adreno 730")

# Access and modify attributes using encapsulation
print(phone)
phone.set_price(950)
print(phone)

# Using the child class methods
print(gaming_phone)
print(gaming_phone.play_game("Call of Duty Mobile"))
