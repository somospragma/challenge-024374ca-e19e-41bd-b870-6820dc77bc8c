import pytest
from src.vehicle import Vehicle
from src.car import Car
from src.motorcycle import Motorcycle
from src.truck import Truck

def test_vehicle_info():
    vehicle = Vehicle("Toyota", "Corolla", 2020)
    assert vehicle.get_info() == "Brand: Toyota, Model: Corolla, Year: 2020"

def test_car_info():
    car = Car("Ford", "Mustang", 2019, 2)
    assert car.get_info() == "Brand: Ford, Model: Mustang, Year: 2019, Number of Doors: 2"

def test_motorcycle_info():
    motorcycle = Motorcycle("Harley", "Davidson", 2018, True)
    assert motorcycle.get_info() == "Brand: Harley, Model: Davidson, Year: 2018, Has Sidecar: True"

def test_truck_info():
    truck = Truck("Volvo", "FH", 2017, 10000)
    assert truck.get_info() == "Brand: Volvo, Model: FH, Year: 2017, Cargo Capacity: 10000"