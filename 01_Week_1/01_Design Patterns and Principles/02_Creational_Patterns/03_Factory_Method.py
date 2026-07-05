from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def type(self):
        pass


class Car(Vehicle):
    def type(self):
        return "Car"


class Bike(Vehicle):
    def type(self):
        return "Bike"


class VehicleFactory:

    @staticmethod
    def create_vehicle(choice):
        if choice == "car":
            return Car()
        elif choice == "bike":
            return Bike()


vehicle = VehicleFactory.create_vehicle("car")
print(vehicle.type())