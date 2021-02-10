class Student:
    def __init__(self, idnum, name, dob, classification):
        self.idnum = idnum
        self.name = name
        self.dob = dob
        self.classification = classification

    def when_register(self):
        if self.classification == "Sr":
            print("Seniors register 11/1-11/3")
        elif self.classification == "Jr":
            print("Juniors register 11/4-11/6")
        elif self.classification == "S":
            print("Sophomores register 11/7-11/9")
        elif self.classification == "F":
            print("Freshman register 11/10-11/12")
        else:
            print("Invalid classification")
