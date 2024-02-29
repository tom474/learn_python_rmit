class Student(object):
    def __init__(self, name, age, GPA):
        self.name = name
        self.age = age
        self.GPA = GPA

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_GPA(self, GPA):
        self.GPA = GPA

    def __str__(self):
        return "Student name: " + self.name + ", age " + str(self.age) + ", GPA: " + str(self.GPA)


def main():
    """Main program"""
    stud = Student("Jessa", 20, 3.2)
    print(stud)

    stud.set_GPA(2.9)
    print(stud)

    stud.set_name("Jessia")
    print(stud)


main()
