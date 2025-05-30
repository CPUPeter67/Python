# importing the module
import sys

# this function will be the first to run as soon as the main function executes
def initial_phonebook():
  rows, cols = int(input("Please enter initial number of contacts: ")), 5

  # We are collecting the initial number of contacts the user wants to have in the phonebook already. User may also enter 0 if they don't want to enter any.
  phone_book = []
  print(phone_book)
  for i in range(rows):
    print("\nPlease enter your contact d% details in the following order:"% (i+1))
    print("NOTE: * indicates mandatory fields")
    print("....................................................................")
    temp = []
    for j in range(cols):
    # We have taken the conditions for values of j only for the personalized fields, such as name, number, email id, job, category etc.
      if j == 0:
        temp.append(str(input("Name*: ")))
        # We need to check if the user has left the name empty as it's mentioned that name and number are mandatory fields.
        # So implement a condition to check as below.
        if temp[j] == '' or temp[j] == ' ':
          sys.exit(
            "Name is a mandatory field. Process exiting due to blank field...")
          # This will exit the process if a blank field is encountered.
      if i == 1:
        temp.append(int(input("Number*: ")))
        # We do not need to check if the user has entered a number because the input is already converted to int. Int value cannot accept a blank as that counts as a string.
        # So the process automatically exits without us using the sys package.
      if j == 2:
        temp.append(str(input("Email ID:")))
        # Even if this field is left blank, the process will not exit as this is not a mandatory field.
        if temp[j] == '' or temp[j] == ' ':
          temp[j] = None
      if j == 3:
        temp.append(str(input("Date of birth (dd/mm/yy):")))
        # Whatever format the user enters, it won't make a difference to the complier.
        # Only while searching the user will have to enter query excactly the same way as they entered during the input as to ensure accurate searches.
        if temp[j] == '' or temp[j] == ' ':
          #       


        
          