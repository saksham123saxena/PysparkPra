'''
- oops : object oriented programming system
- everything in python is object of class
- class name should be start with capital letter
- self argument : it is just a reference to the current instance of class
- __init__ : it will be called each time the class is getting instantiated or object of that class called
'''
class Person:
    def __init__(self,age):
        self.age=age # way of assigning age for all common variable and methode
        print("this is the instantiated methode for this class & value of class "+str(self.age))


    # methode inside the Person class
    def sleep(self): # first argument should be self
        print("person in sleeping mode")

    def argument_exp(self,h):
        return str("numbers of minutes "+str(h*60))


# way of creating the object of the class
# p = Person()
# print(type(p))
# p.sleep()
# print(p.argument_exp(2))
# print("==")

p1=Person(9)

