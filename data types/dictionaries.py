'''In Python, dictionaries are mutable data structures that allow you to store key-value pairs.'''

capitals = {
    "India": "New Delhi",
    "USA": "Washington DC",
    "China": "Beijing"
    
} # don't forget to seperate each one of them with a comma

print(capitals["India"])

print(capitals.get("China")) # this will not throw an error even if the key is not in the dictionary

print(capitals.keys()) # for printing only keys

print(capitals.items()) # for printing all the items 

print(capitals.values()) # for printing the values only

capitals.update({"Germany": "Berlin"})

for key, value in capitals.items():
    print(key + ": " + value)


print(capitals.pop("Germany"))

 