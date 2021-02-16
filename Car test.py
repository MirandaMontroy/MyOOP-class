import CarClass as c


def main():

    my_car = c.Car(2019, "Toyota")

    for x in range(5):
        my_car.accelerate()
        print("Current accelerating speed is", my_car.get_speed())

    print()

    for x in range(5):
        my_car.brake()
        print("Current braking speed is", my_car.get_speed())


main()