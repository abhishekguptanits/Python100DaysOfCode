class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="Nissan", model="GT-R")


# print(my_car.make)
# print(my_car.model)

# # Below line will throw error
# my_car_1 = Car(make="Hyundai")
# print(my_car_1.make)

class ModernCar:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_modern_car = ModernCar(make="Nissan")
print(my_modern_car.make)
print(my_modern_car.model)      # Will print None
