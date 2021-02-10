import random


class Insect:
    def __init__(self):
        self.__wings = 2
        self.__legs = 4
        self.__distance = 0

    def flight_distance(self):
        self.__distance = random.randint(1, 10)

    def get_distance(self):
        return self.__distance
