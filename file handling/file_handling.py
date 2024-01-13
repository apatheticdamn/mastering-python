'''
File handling is an integral part of programming. File handling in Python is simplified with built-in methods, which include creating, opening, and closing files. While files are open, Python additionally allows performing various file operations, such as reading, writing, and appending information.

open("file name", "permission")

a = append
w = write
r = read
'''


#creating a file
text = "Hello my name is Kush and I love Mai Sakurajima"
file = open("c:/My Projects/python/learning python/file handling/Intro.txt", "w") # we can create a file on a specific directory
file.write(text)
print("File created")
file.close()


#reading a file
file = open("c:/My Projects/python/learning python/file handling/Intro.txt", "r")
file_content = file.read()
print(file_content)
file.close()

#writing a file
l1 = ['Mai Sakurajima', "Fubuki", "Fami", "Shinomiya", 'Mitsuha', "Hina"]
file = open('c:/My Projects/python/learning python/file handling/Wifus.txt', "w")
file.writelines(l1)
file.close()

#appending something in the file
string = " senpai"
file = open("c:/My Projects/python/learning python/file handling/Intro.txt", "a")
file.write(string)
file.close()

#readling lines in a file
file = open("c:/My Projects/python/learning python/file handling/Intro.txt", "r")
print(file.readlines())
file.close()

text2 = "Hello world"
file = open("c:/My Projects/python/learning python/file handling/Hello world.txt", "w") #for writing file
file.write(text2)

file = open("c:/My Projects/python/learning python/file handling/Hello world.txt", "r") #for reading file
print(file.readlines())

text3 = " is the first python program that I wrote"
file = open("c:/My Projects/python/learning python/file handling/Hello world.txt", "a") #for appending something
file.write(text3)
file.close()