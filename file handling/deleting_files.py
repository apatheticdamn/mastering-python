'''
The os. remove() function and the pathlib module can remove a single file. While the os. rmdir() function removes an empty directory and the shutil module removes the non-empty directory in Python.
'''
import os
import shutil


path = "c:/My Projects/python/learning python/file handling/test.txt"
try:
	os.remove(path) #we can also use os.rmdir() for removing an empty directory
except FileNotFoundError:
	print("File not found!")

'''
we can use shutil.rmtree() to delete a non-empty folder
be careful while using this function
this function will delete all the files in the directory
'''