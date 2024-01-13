'''
A quick way of moving a file from one place to another is using shutil.move()
'''
import os
import shutil


source = "c:/My Projects/python/learning python/file handling/Intro.txt"
destination = "c:/My Projects/python/learning python/file handling/Intro2.txt"
	
try:
	if os.path.exists(destination):
		print("The file already exists")
	else:
		os.replace(source, destination) #we could also use shutil.copyfile to copy the file
		print(source, "was moved")

except FileNotFoundError:
	print(source,"was not found")

'''
we can also move any folder with the os.replace method
'''