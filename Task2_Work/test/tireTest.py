import unittest

from tires.carriganTire import CarriganTire
from tires.optoprimeTire import OptoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear=[0.1,0.2,0.9,0.6]
        tire=CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear=[0.1,0.2,0.8,0.6]
        tire=CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

class TestOptoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear=[0.5,0.9,0.9,0.9]
        tire=OptoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear=[0.1,0.2,0.9,0.6]
        tire=OptoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())