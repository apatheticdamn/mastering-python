'''
We use the is_file() function, which is part of the Path class from the pathlib module, or exists() function, which is part of the os. path module, in order to check if a file exists or not in Python.
'''

import os

location = "c:/My Projects/python/learning python/file handling/Intro.txt"

if os.path.exists(location):
	print("That location exists")
	if os.path.isfile(location):
		print("That is a file") #if the location is a directory then this line will not get print
	elif os.path.isdir(location):
		print("That is a folder")


else:
	print("That location doesn't exists")


