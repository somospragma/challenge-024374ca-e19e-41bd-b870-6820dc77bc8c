from src.car import Car
from src.motorcycle import Motorcycle
from src.truck import Truck

class VehicleManagement:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def get_vehicle_info(self, index):
        return self.vehicles[index].get_info()

    def perform_action(self, index, action):
        if action == "honk" and isinstance(self.vehicles[index], Car):
            return self.vehicles[index].honk()
        elif action == "wheelie" and isinstance(self.vehicles[index], Motorcycle):
            return self.vehicles[index].wheelie()
        elif action == "load_cargo" and isinstance(self.vehicles[index], Truck):
            return self.vehicles[index].load_cargo()
        else:
            return "Action not available for this vehicle."