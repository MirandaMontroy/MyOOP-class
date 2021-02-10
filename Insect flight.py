import InsectClass as b


def main():
    my_bug = b.Insect(4, 8, 0)

    print(my_bug.get_wings())
    print(my_bug.get_legs())

    print("This is how far the bug can fly: ", str(my_bug.flight_distance()))


main()
