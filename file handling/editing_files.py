'''
First, we open the file. Then we read it using the read() function.
'''
try:
	with open("c:/My Projects/python/learning python/file handling/Intro.txt", "r") as file:
		print(file.read())
except FileNotFoundError: #we can handle exception if the file doesn't exist
	print("The file was not found")


'''
We can create files and edit them by using x parameter in the open() method
'''

try:
	f = open("c:/My Projects/python/learning python/file handling/Intro.txt", "x") #"x" - Create a file, if the file named test.txt is already there it will generate an error
except FileExistsError:
	print("File already exists!")


text = "Hello how are you, this file is written by Kush"

with open('c:/My Projects/python/learning python/file handling/Intro.txt', 'w') as file: #we can also use r for reading, a for appending something at the end
	file.write(text)
