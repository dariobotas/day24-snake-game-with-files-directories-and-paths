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

PLACEHOLDER = "[name]"

class Letter:
  def __init__(self):
    self.name = ""
    self.letter_body = []

  def read_letter_content(self, file_path):
    with open(file_path, mode="r") as letter:
      content = letter.readlines()
    return content
  
  def extract_name_and_letter_body(self, 
                                   file_path="part6/Input/Letters/starting_letter.txt"):
    content_letter = self.read_letter_content(file_path)
    self.name = content_letter[0]
    for word in content_letter[1:]:
        self.letter_body.append(word)
      
  def write_letter_content(self, name, placeholder=PLACEHOLDER, 
                           file_path="part6/Input/Letters/starting_letter.txt"):
    new_name = self.name.replace(placeholder, name)
    content_to_write = []
    content_to_write.append(new_name)
    for word in self.letter_body:
      content_to_write.append(word)
      
    with open(file_path, mode="w") as letter:
      letter.writelines(content_to_write)


class NamesInvited:
  def __init__(self):
    self.names = ""

  def extract_names(self, file_path):
    with open(file_path) as names:
      extracted_names = names.readlines()
    return extracted_names

  def extracted_names_fixed(self, file_path="part6/Input/Names/invited_names.txt"):
    self.names = self.extract_names(file_path)
    #new_names_list = []
    #for name in names_list:
    #  new_names_list.append(name.strip("\n"))
    for index, name in enumerate(self.names):
      self.names[index] = name.strip("\n")
    return self.names

class MailMerge:
  def __init__(self) -> None:
    self.names = NamesInvited()
    self.letter = Letter()

  def mail_merge(self, file_path_names, file_path_letter, file_path_email, placeholder):
      names_list = self.names.extracted_names_fixed(file_path=file_path_names)
      self.letter.extract_name_and_letter_body(file_path_letter)
      
      for name in names_list:
        new_email_file = file_path_email+name+".txt"
        self.letter.write_letter_content(name, placeholder, new_email_file)
      
    
if __name__ == "__main__":
  mail_merge = MailMerge()
  mail_merge.mail_merge("part6/Input/Names/invited_names.txt", PLACEHOLDER,
                        "part6/Input/Letters/starting_letter.txt","part6/Output/ReadyToSend/")
 #names = NamesInvited()
  #list = names.names
  #letter = Letter()
  #content = letter.extract_name_and_letter_body()
  #print(content)
  #print(list)
  #print(letter.name)
#print(letter.letter_body)

#for content in letter.letter_body:
#  print(content)"""