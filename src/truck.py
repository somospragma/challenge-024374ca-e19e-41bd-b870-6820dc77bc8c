from src.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand, model, year, cargo_capacity):
        super().__init__(brand, model, year)
        self.cargo_capacity = cargo_capacity

    def get_info(self):
        return f"{super().get_info()}, Cargo Capacity: {self.cargo_capacity}"

    def load_cargo(self):
        return "Cargo Loaded!"