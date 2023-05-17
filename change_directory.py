"""
Change directory
"""

#Import statement: operating system interfaces
import os

#Obtain current working directory
path = os.getcwd()

#Show current working directory
print(path)

#Path using a raw string
new_path = r"C:\Users\User"

#Change directory
os.chdir(new_path)
print(os.getcwd())

