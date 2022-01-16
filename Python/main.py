from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola Mundo")

    car = Car("B6E-482", Account("Luis Rueda", "70059584"))
    print(vars(car))
    print(vars(car.driver))