'''Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.

base class = parent class
derived class = child class
'''


class Mammal:
    have_four_limbs = True
    have_hair = True
    heart_chambers = 4


class Animal:  # base class
    alive = True  # class variable

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Cat(Animal, Mammal):  # derived class
    def meow(self):
        print("This cat is Meowing")


class Dog(Animal, Mammal):  # derived class
    def bark(self):
        print("This dog is barking")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.sleep()
cat.meow()

print(dog.alive)
print(cat.alive)

print(dog.have_hair)
print(dog.heart_chambers)
