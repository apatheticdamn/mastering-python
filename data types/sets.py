'''
A Set in Python programming is an unordered collection data type that is iterable, mutable and has no duplicate elements.
'''

operating_systems1 = {"Microsoft Windows", "Linux", "MacOS", "Android", "Ubuntu"} # if you will print a set it might not be in this order because sets are unordered, their order will change everytime you run the code

for os in operating_systems1:
    print(os) 


operating_systems1.add("Black Arch") # sets are unchangeable however you can add or remove items 
print(operating_systems1)

operating_systems1.remove("MacOS")
print(operating_systems1)

operating_systems2 = {"Solaris", "Fedora", "ChromeOS", "Microsoft Windows", "Linux"}

print(operating_systems1.intersection(operating_systems2)) # this will return the elements that are common in both the sets


operating_systems1.update(operating_systems2) # we can also update the set and we could also use the .union() method

print("Updated set:\n", operating_systems1)