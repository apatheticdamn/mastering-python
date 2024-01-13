'''
To copy the contents of a file object to another specified destination file object, use the shutil. copyfile() method. This method takes two file objects as arguments – a source file object and a destination file object. The destination cannot be a directory.

copyfile() = copies contents of a file

copy() = copyfile() + permission mode + destination can be a directory

copy2() = copy + copies metadata (file's creation and modification times)
'''

import shutil

shutil.copyfile("c:/My Projects/python/learning python/file handling/Wifus.txt", "c:/My Projects/python/learning python/file handling/copied_test.txt")

 






