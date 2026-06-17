from src.vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        return f"{super().get_info()}, Has Sidecar: {self.has_sidecar}"

    def wheelie(self):
        return "Wheelie!"