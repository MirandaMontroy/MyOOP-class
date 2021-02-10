import random


class Insect:
    def __init__(self, w, l, f):
        self.__wings = w
        self.__legs = l
        self.__distance = f

    def flight_distance(self):
        self.__distance = random.randint(1, 10)
        return self.__distance

    def get_wings(self):
        return self.__wings

    def get_legs(self):
        return self.__legs

    def __str__(self):
        return print(
            "wings:",
            str(self.__wings),
            "\n",
            "legs:",
            str(self.__legs),
            "\n",
            "flight:",
            str(self.__distance),
        )
