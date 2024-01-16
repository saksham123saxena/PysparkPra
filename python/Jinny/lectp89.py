"""
class and object
"""


class Instructor:
    pass


class InstructorV1:
    def __init__(self, name, address):
        self.name = name
        self.address = address


instructor_1 = Instructor()
print(type(instructor_1))
instructor_1.name = "hello"
instructor_1.roll = 2
print(instructor_1.name)
print("-------------------------------------------\n")

instructor_2 = InstructorV1("payal", "delhi")
print(instructor_2.name)
print(f"info of instructor_2 object info : {instructor_2.name} and {instructor_2.address}")
