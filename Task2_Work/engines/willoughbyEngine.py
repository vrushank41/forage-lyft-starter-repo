from engines.engine_parent import Engine

class WilloughbyEngine(Engine):
    current_mileage:int
    last_service_mileage:int

    def __init__(self,current_mileage,last_service_mileage):
        super().__init__()
        self.current_mileage=current_mileage
        self.last_service_mileage=last_service_mileage

    def needs_service(self):
        return self.current_mileage-self.last_service_mileage>60000