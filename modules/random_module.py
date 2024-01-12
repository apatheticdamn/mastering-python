'''
Python Random module is an in-built module of Python that is used to generate random numbers in Python. These are pseudo-random numbers means they are not truly random. This module can be used to perform random actions such as generating random numbers, printing random a value for a list or string, etc
'''

import random


a = random.randint(1, 10)
b = random.random()
print(a)
print(b)


my_list = ['rock', 'paper', 'scissors']
my_list = random.choice(my_list)
print(my_list)


cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "K", "Q", "A"]
random.shuffle(cards)
print(cards)

