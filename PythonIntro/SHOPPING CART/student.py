from person import Person:


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init(self, fname, lname)

    