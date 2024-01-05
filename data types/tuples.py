'''
Tuples are used to store multiple items in a single variable. A tuple is an immutable (unchangeable) object, which means it cannot be changed, and we use it to represent fixed collections of items.
'''

flagship_phones = ("Samsung Galaxy S23 Ultra", "Asus Rog 7", "Red Magic 8 Pro")

print(flagship_phones.count("Red Magic 8 Pro"))
print(flagship_phones.index("Asus Rog 7"))

if "Samsung Galaxy S23 Ultra" in flagship_phones:
    print("Yes it is")