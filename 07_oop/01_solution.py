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

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"

# myCar = Car("Toyota", "Corolla")

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size


# myElectricCar = ElectricCar("Tesla", "Model 3", "75 kWh")
# print(myElectricCar.brand)
# print(myElectricCar.model)
# print(myElectricCar.battery_size)
# print(myElectricCar.full_name())




# 4 Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
    
#     def get_brand(self):
#         return self.__brand

#     def full_name(self):
#         return f"{self.__brand} {self.model}"

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size


# myElectricCar = ElectricCar("Tesla", "Model 3", "75 kWh")
# # print(myElectricCar.brand)
# # print(myElectricCar.model)
# # print(myElectricCar.battery_size)
# # print(myElectricCar.full_name())

# print(myElectricCar.get_brand())


#Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
    
#     def get_brand(self):
#         return self.__brand

#     def full_name(self):
#         return f"{self.__brand} {self.model}"
    
#     def fuel_type(self):
#         return "Petrol or Diesel"

# myCar = Car("Toyota", "Corolla")


# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electricity"


# myElectricCar = ElectricCar("Tesla", "Model 3", "75 kWh")
# # print(myElectricCar.brand)
# # print(myElectricCar.model)
# # print(myElectricCar.battery_size)
# # print(myElectricCar.full_name())

# print(myElectricCar.get_brand())
# print(myElectricCar.fuel_type())
# print(myCar.fuel_type())


# Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

# class Car:
#     total_cars = 0

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
#         Car.total_cars += 1 #self.total_cars += 1 would also work but it would create an instance variable instead of modifying the class variable
    
#     def get_brand(self):
#         return self.__brand
    
#     def full_name(self):
#         return f"{self.__brand} {self.model}"
    
#     def fuel_type(self):
#         return "Petrol or Diesel"
    
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electricity"

# tesla = ElectricCar("Tesla", "Model 3", "75 kWh")
# toyota = Car("Toyota", "Corolla")
# print(tesla.total_cars)

# Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1 
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electricity"