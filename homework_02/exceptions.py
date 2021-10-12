class LowFuelError(Exception):
    """ Exception Low Fuel Error
    """
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "Low Fuel Error"
    
    def __str__(self):
        return f"LowFuelError, {self.message}"

    
class NotEnoughFuel(Exception):
    """Exception Not Enough Fuel
    """
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "Not Enough Fuel"
    
    def __str__(self):
        return f"NotEnoughFuel, {self.message}"

class CargoOverload(Exception):
    """Exception Cargo Overload
    """
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "Cargo Overload"
    
    def __str__(self):
        return f"CargoOverload, {self.message}"

