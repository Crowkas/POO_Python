from car import Car

class UberVan(Car):
    brand = str
    model = str

    def __init__(self, license, driver, typeCarAccepted, seatsMaterial):
        super().__init__(license, driver)
        self.brand = typeCarAccepted
        self.model = seatsMaterial