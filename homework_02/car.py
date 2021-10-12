from homework_02.base import Vehicle


class Car(Vehicle):
    """ Class Car
    """
    def __init__(self, weight, fuel, fuel_consumption):
        """Init car
        """
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    
    def set_engine(self, engine):
        """ Set engine car
        """
        self.engine = engine