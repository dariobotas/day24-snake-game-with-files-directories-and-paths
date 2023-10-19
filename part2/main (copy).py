"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

#import part7.game

#to open file
file = open("my_file.txt")
#to read content and print on console screen
content = file.read()
print(content)
#close it after use it
file.close()

#a way to do previous steps
with open("my_file.txt") as file:
  contents = file.read()
  print(contents)

#this rewrite the file. Clean everyting and write what we want
with open("my_file.txt", mode="w") as file:
  file.write("New text")

#This append to the file
with open("my_file.txt", mode="a") as file:
  file.write("\nNew text")

#This append to the file. The file doesn't exist and is created
with open("new_file.txt", mode="a") as file:
  file.write("\nNew text")