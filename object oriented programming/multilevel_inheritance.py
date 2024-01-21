'''
In python, Multilevel inheritance is one type of inheritance being used to inherit both base class and derived class features to the newly derived class when we inherit a derived class from a base class and another derived class from the previous derived class up to any extent of depth of classes in python is called multilevel inheritance.
'''

class Organism:
    breathe = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating...")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")


dog = Dog()
print(dog.breathe)

dog.eat()
dog.bark()