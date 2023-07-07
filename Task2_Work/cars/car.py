from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery

    @property
    def engine(self):
        """Returns the car's engine."""
        return self._engine

    @property
    def battery(self):
        """Returns the car's battery."""
        return self._battery

    def needs_service(self):
        """Returns True if the car needs service, False otherwise."""
        # Check the car's engine and battery to determine if it needs service.
        return True
