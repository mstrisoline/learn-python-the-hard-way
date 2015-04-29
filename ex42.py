#!/usr/bin/env python

##Animal is a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

##??
class Dog(Animal):
    def __init__(self, name):
        ##??
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        ##Person has a pet of some kind
        self.pet = None

##??
class Employee(Person):
    def __init__(self, name, salary):
        ##?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ##??
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

##rover is a Dog
rover = Dog("Rover")
print rover
##??
satan = Cat("Satan")
print satan

##??
mary = Person("Mary")
print mary
mary.pet = satan
print mary.pet
frank = Employee("Frank", 120000)
print frank
frank.pet = rover
print frank.pet
flipper = Fish()
print flipper
crouse = Salmon()
print crouse
harry = Halibut()
print harry
