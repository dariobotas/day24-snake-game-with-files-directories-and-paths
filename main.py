"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#import part6.main    

PLACEHOLDER = "[name]"

if __name__ == "__main__":
  with open("part6/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

  with open("part6/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
      stripped_name = name.strip("\n")
      new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
      with open(f"part6/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as letter:
        letter.write(new_letter)
        

  