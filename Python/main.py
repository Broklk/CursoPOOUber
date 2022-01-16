from car import Car

if __name__ == "__main__":
    print("Hola Mundo")

    car = Car()
    car.license = "B6E-482"
    car.driver = "Luis Rueda"
    print(vars(car))

    car2 = Car()
    car2.license = "AN-1212"
    car2.driver = "Karen Moril"
    print(vars(car2))