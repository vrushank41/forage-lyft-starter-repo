from tires.tire_parent import Tire

class CarriganTire(Tire):
    def __init__(self,tire_wear):
        self.tire_wear=tire_wear
    def needs_service(self):
        for val in self.tire_wear:
            if val>=0.9:
                return True
            else:
                return False

