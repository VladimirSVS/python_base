from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    
    def __init__(self, weight: int = 0, fuel: int = 0, fuel_consumption: int = 7):
        """ Init
        """
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self, started: bool = False):
        """Started
        """
        if not started:
            try:
                if self.fuel > 0:
                    self.started = True
                else:
                    raise exceptions.LowFuelError
            except exceptions.LowFuelError:
                raise

    def move(self, weight: int):
        """ Move Vehicle
        """
        fuel = self.fuel
        fuel_consumption = self.fuel_consumption
        try:
            fuel_required = fuel - weight * fuel_consumption
            if fuel < fuel_required or fuel_required < 0:
                self.fuel = 0
                raise exceptions.NotEnoughFuel
            else:
                self.fuel = fuel_required
        except exceptions.NotEnoughFuel:
            raise