from src.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def get_info(self):
        return f"{super().get_info()}, Number of Doors: {self.num_doors}"

    def honk(self):
        return "Honk!"