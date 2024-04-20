import random
import string

def generate_password(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters #all uppercasse and lower case letters
    digits = string.digits #all digits
    special = string.punctuation #all special characters

    # print(letters, digits, special)

    #now we need need to combine all of this in a list to randomly choose from to create a password

    characters = letters #since letters are always a part of the password

    #if numbers = true
    if numbers:
        characters += digits

    #if special_characters is true
    if special_characters:
        characters += special

    pwd = "" #empty string for password generation
    meets_criteria = False #means its a valid password based on input of the function
    has_number = False
    has_special = False

    #loops till meet criteria is false or length of password is < min_length
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    
    return pwd

min_length = int(input("Enter the minimum length: "))
numbers = input("Do you want to have numbers? (Y/N)").lower() == "y" #if y then true else saves false
special_characters = input("Do you want to have special characters? (Y/N)").lower() == "y" #if y then true else saves false

pwd = generate_password(min_length, numbers, special_characters)
print("The generated password is: ", pwd)
