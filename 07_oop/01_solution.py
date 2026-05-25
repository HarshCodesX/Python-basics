# Question 1 - Create a Car class with attributes like brand and model. Then create an instance of this class.

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# myCar = Car("Toyota", "Corolla")
# print(myCar.brand)
# print(myCar.model)

# question 2 - Add a method to the Car class that displays the full name of the car (brand and model).

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"

# myCar = Car("Toyota", "Corolla")
# print(myCar.brand)
# print(myCar.model)
# print(myCar.full_name())

# Question 3 Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

myCar = Car("Toyota", "Corolla")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


myElectricCar = ElectricCar("Tesla", "Model 3", "75 kWh")
print(myElectricCar.brand)
print(myElectricCar.model)
print(myElectricCar.battery_size)
print(myElectricCar.full_name())