from car import Car 
from account import Account
from uberBlack import UberBlack
from uberVan import UberVan
from uberPool import UberPool
from uberX import UberX

if __name__ == "__main__":
    print('Hola mundo')

car = Car('CEG673', Account('Andres Herrera', 'ANU683'))
print(vars(car))
print(vars(car.driver))

uberX = UberX('HTJ235', 'Andres Herrera', 'Chevrolet', 'Spark')
print(vars(uberX))
print(vars(car.driver))
