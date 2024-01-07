'''
Lists are used to store multiple items in a single variable
'''


wifus = ["Mai sakurajima", "Fubuki", "Chizuru", "Boa Hancock", "Robin", "Zero Two", "Shinomiya", "Mikasa", "Yor Forger", "Mitsuri", "Makima"]

for wifu in wifus: # for printing every list items on a new line
    print(wifu)

print() # for one line space

wifus[10] = "Power" # remeber that index always start from 0
print(wifus, "\n")

wifus.append("Akeno",) # for adding something at the end of the list
print(wifus, "\n")

wifus.remove("Mitsuri") # for removing something from the list
print(wifus, "\n")

wifus.append("Mitsuri") # i will add her again cuz i can't remove her from my wifu list

wifus.sort() # this will sort the list alphabetically
print(wifus, "\n")

wifus.reverse() # this will reverse the list
print(wifus, "\n")

