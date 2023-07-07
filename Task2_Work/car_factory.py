from datetime import date
from cars.car import Car
from engines.capuletEngine import CapuletEngine
from engines.willoughbyEngine import WilloughbyEngine
from engines.sternmanEngine import SternmanEngine

from batteries.nubbinBattery import NubbinBattery
from batteries.spindlerBattery import SpindlerBattery

class CarFactory:

    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date,last_service_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        return Car(engine, battery)
    
# car = CarFactory.create_calliope(date.today(),date.today().replace(year=date.today().year - 3),50000,30000)
# print("Calliope needs to be serviced:",car)

    