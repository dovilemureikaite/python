# MOD04_1-6.1_Intro_Python.ipynb
# ___________________________________________________________________________________
#
# TASK 1
# ________________________
# [ ] Say "Hello" with nested if
# [ ] Challenge: handle input other than y/n
answer = input('Say "Hello" ? (yes/no)')

if answer.lower() == "yes":
    answer = input('Full "Hello" ?')
    if answer.lower() == "yes":
        print('"Hello"')
    elif answer.lower() == "no":
        print('"Hi"')
    else:
        print("Please answer correctly ! (yes/no)")
elif answer.lower() == "no":
    print('"(friendly nod)"')
else:
    print('Wrong answer : enter "yes" or "no"')

# TASK 2
# _________________________
# Program: [ ] 3 Guesses
# use nested if statements complete the flowchart code
# create a birds string variable with the names of 1, 2, 3 or more birds to make it easier
# get bird_guess input and use bird_guess in bird_names to generate Boolean True/False
# if the the guess is wrong (False) create a sub test until the user has had 3 guesses

# [ ] Create the "Guess the bird" program 
bird_names = "parrot, eagle, magpie"
bird_guess = input("Guess a bird's name: (1st try)").lower()

if bird_guess in bird_names:
    print("Yes, 1st try ! It's a",bird_guess)
else:
    bird_guess = input("Guess a bird's name: (2nd try)").lower()
    if bird_guess in bird_names:
        print("Yes, 2nd try. It's a",bird_guess)
    else:
        bird_guess = input("Guess a bird's name: (3rd try)").lower()
        if bird_guess in bird_names:
            print("Yes, 3rd try. It's a",bird_guess)
        else:
            print("Sorry, out of tries")
# ____________________________

# MOD04_1-6.2_Intro_Python.ipynb
# _____________________________________________________________________________________

# TASK 1
# ________________________
# [ ] print "\\\WARNING!///"
print("\\\\\\WARNING!///")

# _________________________
# [ ] print output that is exactly (with quotes): "What's that?" isn't a specific question.
print("\"What\'s that?\" isn\'t a specific question.")

# __________________________
# [ ] from 1 print statement output the text commented below using no spaces
# One     Two     Three
# Four    Five    Six
print("One\tTwo\tThree\nFour\tFive\tSix")

# __________________________

# TASK 2
# __________________________
# Program: pre_word() Function
# Function has a single string parameter that it checks s is a single word starting with "pre"
#
# Check if word starts with "pre"
# Check if word .isalpha()
# if all checks pass: return True
# if any checks fail: return False
# Test
# get input using the directions: *enter a word that starts with "pre": *
# call pre_word() with the input string
# test if return value is False and print message explaining not a "pre" word
# else print message explaining is a valid "pre" word

# [ ] create and test pre_word()
def pre_word(str):
    if str.isalpha():
        if str.startswith("pre"):
            return True
        else:
            return False
    return False
# end function

word = input("Enter a word that starts with \"pre\"").lower()
if pre_word(word) == False:
    print("NOT a \"pre\" word")
else:
    print("VALID \"pre\" word")

# TASK 5 (there is a mistype in the task name, it should be TASK 3)
# _______________________________
# [ ] review, run, fix
print("Hello" + "\n" + "World!")

# _______________________________
#
# Practice_MOD04_1-6_IntroPy.ipynb
# _______________________________________________________________________________
#
# TASKS
# ____________________
# [ ] print a string that outputs the following exactly: The new line character is "\n"
print("The new line character is \"\\n\"")

# ____________________
# [ ] print output that is exactly (with quotes): "That's how we escape!"
print("\"That\'s how we escape!\"")

# ____________________
# [ ] with only 1 print statement and using No Space Characters, output the text commented below  

# 1       one
# 22      two
# 333     three

print("1\tone\n22\ttwo\n333\tthree")

# ______________________
# Program: quote_me() Function
# quote_me takes a string argument and returns a string that will display surrounded with added double quotes if printed
#
# check if passed string starts with a double quote ("\""), then surround string with single quotations
# if the passed string starts with single quote, or if doesn't start with a quotation mark, then surround with double quotations
# Test the function code passing string input as the argument to quote_me()

# [ ] create and test quote_me()
def quote_me(str):
    if str.startswith("\""):
        print("\'"+str+"\'")
    elif str.startswith("\'"):
        print("\""+str+"\"")
    else:
        print("\""+str+"\"")
#end function

test = input("Enter some words to test: ")
quote_me(test)

# _______________________
# Program: shirt order
# First get input for color and size
#
# White has sizes L, M
# Blue has sizes M, S
# print available or unavailable, then
# print the order confirmation of color and size
#
# * hint: set a variable "available = False" before nested if statements and
# change to True if color and size are avaliable*

# [ ] create shirt order using nested if 
color = input("Enter color: ").capitalize()
size = input ("Enter size:").upper()
available = False

if color == "White":
    if size == "M":
        available = True
        print()
        print("Order confirmation: \n\nCOLOR:\t\t" + color + "\nSIZE:\t\t" + size + "\nAVAILABLE:\t" + str(available))
    elif size == "L":
        available = True
        print()
        print("Order confirmation: \n\nCOLOR:\t\t" + color + "\nSIZE:\t\t" + size + "\nAVAILABLE:\t" + str(available))
    else:
        print()
        print("Order confirmation: \n\nCOLOR:\t\t" + color + "\nSIZE:\t\t" + size + "\nAVAILABLE:\t" + str(available))
elif color == "Blue":
    if size == "S":
        available = True
        print()
        print("Order confirmation: \n\nCOLOR:\t\t" + color + "\nSIZE:\t\t" + size + "\nAVAILABLE:\t" + str(available))
    elif size == "M":
        available = True
        print()
        print("Order confirmation: \n\nCOLOR:\t\t" + color + "\nSIZE:\t\t" + size + "\nAVAILABLE:\t" + str(available))
    else:
        print()
        print("Order confirmation: \n\nCOLOR:\t\t" + color + "\nSIZE:\t\t" + size + "\nAVAILABLE:\t" + str(available))
else:
    print()
    print("WRONG ORDER ! Invalid value !")

# _________________________________
# Program: str_analysis() Function
# Create the str_analysis() function that takes a string argument. In the body of the function:
#
# Check if string is digits
# if digits: convert to int and check if greater than 99
# if greater than 99, print a message about a "big number"
# if not greater than 99, print message about "small number"
# if not digits: check if string isalpha
# if isalpha print message about being all alpha
# if not isalpha print a message about being neither all alpha nor all digit
# call the function with a string from user input

# [ ] create and test str_analysis()
def str_analysis(user_str):
    if user_str.isdigit():
        if int(user_str) > 99:
            print("\n",user_str,"is a BIG number")
        else: 
            print("\n",user_str,"is a SMALL number")
    else:
        if user_str.isalpha():
            print("\n",user_str,"\n\nAll alpha")
        else:
            print("\nNeither all alpha nor all digit")    
#end function   

str = input("Enter a string:")
str_analysis(str)

# ______________________________
# Program: ticket_check() - finds out if a seat is available
# Call ticket_check() function with 2 arguments: section and seats requested and return True or False
# 
# section is a string and expects: general, floor
# seats is an integer and expects: 1 - 10
# Check for valid section and seats

# if section is general (or use startswith "g")
# if seats is 1-10 return True
# if section is floor (or use starts with "f")
# if seats is 1-4 return True
# otherwise return False

# [ ] create and call ticket_check()
def ticket_check(section,seats):
    if section == "general":
        if seats.isdigit():
            if (int(seats) >= 1) and (int(seats) <= 10):
                return True
            else:
                return False
        else:
            return False
    elif section == "floor":
        if seats.isdigit():
            if (int(seats) >= 1) and (int(seats) <= 4):
                return True
            else:
                return False
        else:
            return False
    else:
        return False   

req_section = input("Enter section: ")
req_seats = input("Enter seats: ")
print()
print("AVAILABLE:",ticket_check(req_section,req_seats))

# ________________________
