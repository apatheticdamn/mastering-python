'''
String formatting is also known as String interpolation. It is the process of inserting a custom string or variable in predefined text.

str.format()  optional method thata gives users more control when displaying output
'''

name = "Kush"
sentence = "you're the best coder in the world"

print("Hi, {}! I think that {}".format(name,sentence))
print("Hi, {0}! I think that {1}".format(name, sentence))

# we can also add some padding 
print("Hi, {:3}! I think that {:4}. We are going to hire you!".format(name, sentence))

num1 = 1000

# we can also print number systems in python
print("The number in decimal: {:d}".format(num1))
print("The number is binary: {:b}".format(num1))
print("The number in hexadecimal: {:x}".format(num1)) # we can use uppercase X for uppercase hexadecimal values
print("The number in octal: {:o}".format(num1))

# some cool methods
print("The number is {:,}".format(num1)) # this will add comma (,) to all 1000s places

# or we can pass keyword argument like this
# print("Hi {}! I think that {}".format(name="Kush", sentence="is the most handsome person in the world"))
