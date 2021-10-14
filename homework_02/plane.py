from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    """Class Plane
    """
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        """Init plane
        """
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo


    def load_cargo(self,num: int):
        """Load cargo
        """
        if num + self.cargo <= self.max_cargo:
            self.cargo += num
        else:
            raise exceptions.CargoOverload

    
    def remove_all_cargo(self):
        """Remove all cargo
        """
        before_cargo = self.cargo
        self.cargo = 0
        return before_cargo
