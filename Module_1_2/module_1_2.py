# MOD01_1-2.1_Intro_Python.ipynb
# ________________________________________
# TASK 1
# ____________________
# [ ] get input for the variable student_name
student_name = input()
# [ ] determine the type of student_name
type(student_name)

# [ ] run cell several times entering a name a int number and a float number after adding code below
print("enter a name or number")
test_input = input()
# [ ] insert code below to check the type of test_input
type(test_input)

# TASK 2
# _____________________
# [ ] get user input for a city name in the variable named city
city = input("Enter city name : ")
# [ ] print the city name
print("The city name is " + city)

# [ ]create variables to store input: name, age, get_mail with prompts
# for name, age and yes/no to being on an email list
name = input("Enter your name : ")
age = input("Enter your age : ")
get_mail = input("Want to be in the email list ? : ")

# [ ] print a description + variable value for each variable
print("____________")
print("name = " + name)
print("age = " + age)
print("wants email = " + get_mail)

# MOD01_1-2.2_Intro_Python.ipynb
# __________________________________________

# TASK 1
# _____________________
# [ ] print 3 strings on the same line using commas inside the print() function 
print("Pirmas","Antras","Trecias")

# TASK 2
# _____________________
# [ ] use a print() function with comma separation to combine 2 numbers and 2 strings
print("Skaicius = ",17,"yra nelyginis, o skaicius",4,"yra lyginis")

# TASK 3
# ______________________
# [ ] get user input for a street name in the variable, street
street = input("Enter street name : ")
# [ ] get user input for a street number in the variable, st_number
st_number = input("Enter street number : ")
# [ ] display a message about the street and st_number
print("Street name = ",street,"and street number is",st_number)

# TASK 4
# ______________________
# [ ] define a variable with a string or numeric value
random = "amazing"
# [ ] display a message combining the variable, 1 or more literal strings and a number
print("This day is ",random,"because temperature is",19,"degrees celsius")

# TASK 5
# ______________________
# [ ] get input for variables: owner, num_people, training_time  - use descriptive prompt text
owner = input("Please enter your name : ")
num_people = input("Please enter the number of students : ")
training_time = input("Please enter time of the trainings : ")
# [ ] create a integer variable min_early and "hard code" the integer value (e.g. - 5, 10 or 15)
min_early = 15
# [ ] print reminder text using all variables & add additional strings -  use comma separated print formatting
print("___________________________________________________________________")
print("Hello",owner,",")
print("you have training class at",training_time,".")
print("It's recommended to come",min_early,"min. earlier before the trainings start")

# MOD01_1-2.3_Intro_Python.ipynb
# __________________________________________

# TASK 1
# _____________________
# [ ] using a print statement, display the text: Where's the homework?
print("Where's the homework ?")
# [ ] output with double quotes: "Education is what remains after one has forgotten what one has learned in school" - Albert Einstein
print('"Education is what remains after one has forgotten what one has learned in school" - Albert Einstein')

# TASK 2
# _____________________
# [ ] Use .isalpha() on the string "alphabetical"
"alphabetical".isalpha()
# [ ] Use .isalpha() on the string: "Are spaces and punctuation Alphabetical?"
"Are spaces and punctuation Alphabetical?".isalpha()

# [ ] initailize variable alpha_test with input
alpha_test = input("Enter something : ")
# [ ] use .isalpha() on string variable alpha_test
alpha_test.isalpha()

# MOD01_1-2.4_Intro_Python.ipynb
# ___________________________________________

# TASK 1
# ____________________
# [ ] get input for a variable, fav_food, that describes a favorite food
fav_food = input("Your favourite food is :")
# [ ] display fav_food as ALL CAPS, used in a sentence
print(fav_food.upper())

# [ ] dispaly fav_food as all lower case, used in a sentence
print(fav_food.lower())

# [] display fav_food with swapped case, used in a sentence
print(fav_food.swapcase())

# [] display fav_food with capitalization, used in a sentence
print(fav_food.capitalize())

fav_color = "Forest Green"
# [] display the fav_color variable as upper, lower, swapcase, and capitalize formatting in a single print() statement
print("upper:",fav_color.upper(),"lower:",fav_color.lower(),"swapcase:",fav_color.swapcase(),"capitalize:",fav_color.capitalize())

# TASK 2
# ______________________
# [] input variable fav_color as upper
fav_color = input("Your favourite color is :").upper()
# [] print fav_color
print(fav_color)

# TASK 3
# ______________________
# [] print 3 tests, with description text, testing the menu variable for 'pizza', 'soup' and 'dessert'
menu = "salad, pasta, sandwich, pizza, drinks, dessert"
print("'pizza' in menu =",'pizza' in menu)
print("'soup' in menu =",'soup' in menu)
print("'dessert' in menu =",'dessert' in menu)

# Create a program where the user supplies input to search the menu
# **** RUN previous task first !**** (before running this one)
menu = menu + ", kebab"
print("Menu:",menu)
menu_ask = input("Enter item:")
print(menu_ask,"found in menu:",menu_ask.lower() in menu.lower())

# add to menu
print("CURRENT menu:",menu)
add_item = input("Enter item:")
new_menu = menu + ", " + add_item
print("NEW menu:",new_menu)

# Testing Add to Menu - create user input to search for an item on the new menu
item_search = input("Enter item to search:")
print(item_search,"in menu ? =",item_search.lower() in new_menu.lower())

# TASK 4
# ______________________
# [ ] fix the error
# paint_colors = "red, blue, green, black, orange, pink"
# print('Red in paint colors = ',red in paint_colors)

paint_colors = "red, blue, green, black, orange, pink"
print('Red in paint colors = ',"red" in paint_colors)

# Practice_MOD01_1-2_IntroPy.ipynb
# _________________________________
# [ ] get user input for a variable named remind_me
remind_me = input()
# [ ] print the value of the variable remind_me
print("remind_me value:",remind_me)

# use string addition to print "remember: " before the remind_me input string
print("remember:",remind_me)

# [ ] get user input for 2 variables: meeting_subject and meeting_time
meeting_subject = input("what is the meeting subject?:")
meeting_time = input("what is the meeting time?:")
# [ ] use string addition to print meeting subject and time with labels
print("")
print("Meeting Subject:",meeting_subject)
print("Meeting Time:",meeting_time)

# [ ] print combined string "Remember to" and the string variable remind_me from input above
print("Remember to",remind_me)

# [ ] print combined string "Remember to" and the string variable remind_me from input above
print("Remember to",remind_me)

# [ ] Combine 3 variables from above with multiple strings
print("Reminder to",remind_me,"that meeting time is",meeting_time,"and meeting subject will be",meeting_subject)

# [ ] print a string sentence that will display an Apostrophe (')
print("It's a sunny day")

# [ ] print a string sentence that will display a quote(") or quotes
print('"Hello" is a greeting everyone should know')

# [ ] complete vehicle tests 
vehicle = input("enter vehicle:")
print("_____________")
print("All Alpha :",vehicle.isalpha())
print("All Alpha Numerical :",vehicle.isalnum())
print("Capitalized (first letter only) :",vehicle.istitle())
print("All lowercase :",vehicle.islower())
print()

# [ ] print True or False if color starts with "b" 
color_item = input("enter color:")
print('Color stars with "b" :',color_item.lower().startswith("b"))

# [ ] print the string variable capital_this Capitalizing only the first letter
capitalize_this = "the TIME is Noon."
print("result: ",capitalize_this.capitalize())

# print the string variable swap_this in swapped case
swap_this = "wHO writes LIKE tHIS?"
print("result:",swap_this.swapcase())

# print the string variable whisper_this in all lowercase
whisper_this = "Can you hear me?"
print("result:",whisper_this.lower())

# print the string variable yell_this in all UPPERCASE
yell_this = "Can you hear me Now!?"
print("result:",yell_this.upper())

#format input using .upper(), .lower(), .swapcase, .capitalize()
format_input = input('enter a string to reformat (upper): ').upper()
print("upper:",format_input)
format_input = input('enter a string to reformat (lower): ').lower()
print("lower:",format_input)
format_input = input('enter a string to reformat (swapcase): ').swapcase()
print("swapcase:",format_input)
format_input = input('enter a string to reformat (capitalize): ').capitalize()
print("capitalize:",format_input)

# [ ] get user input for a variable named color
# [ ] modify color to be all lowercase and print
named_color = input("Enter color:").lower()
print("result:",named_color)

# [ ] get user input using variable remind_me and format to all **lowercase** and print
# [ ] test using input with mixed upper and lower cases
remind_me = input().lower()
print("result:",remind_me)

# [] get user input for the variable yell_this and format as a "YELL" to ALL CAPS
yell_this = input().upper()
print("result:",yell_this)

# [ ] get user input for the name of some animals in the variable animals_input
animals_input = input("enter:")
# [ ] print true or false if 'cat' is in the string variable animals_input
print("cat in the list ? :","cat" in animals_input.lower())

# [ ] get user input for color
color = input("enter color:")
# [ ] print True or False for starts with "b"
print('starts with "b" ? :',color.lower().startswith("b"))
# [ ] print color variable value exactly as input 
#     test with input: "Blue", "BLUE", "bLUE"
print("entered value:",color)

# project: "guess what I'm reading"
# 1[ ] get 1 word input for can_read variable
can_read = input("Enter 1 word item that can be read:")
# 2[ ] get 3 things input for can_read_things variable
can_read_things = input("Enter 3 items that can be read:")
# 3[ ] print True if can_read is in can_read_things
print("_____")
print(can_read,"found =",can_read in can_read_things)
# [] challenge: format the output to read "item found = True" (or false)
# hint: look print formatting exercises

# Allergy check 
# 1[ ] get input for test
input_test = input("enter somethings eaten in las 24 hrs:")
allergen = input("enter allergen:")
# 2/3[ ] print True if "dairy" is in the input or False if not
print('It is',allergen.lower() in input_test.lower(),'that',input_test,'contains',allergen)
# 4[ ] Check if "nuts" are in the input 
#  Dovile's comment: See step no.1. There is a variable "allergen". You can enter "nuts" there.
# 4+[ ] Challenge: Check if "seafood" is in the input
#  Dovile's comment: See step no.1. There is a variable "allergen". You can enter "seafood" there.
# 4+[ ] Challenge: Check if "chocolate" is in the input
#  Dovile's comment: See step no.1. There is a variable "allergen". You can enter "chocolate" there.

# Required_Code_MOD1_IntroPy.ipynb
# ___________________________________________
# Allergy check 
# 1[ ] get input for test
input_test = input("enter somethings eaten in las 24 hrs:")
allergen = input("enter allergen:")
# 2/3[ ] print True if "dairy" is in the input or False if not
print('It is',allergen.lower() in input_test.lower(),'that',input_test,'contains',allergen)
# 4[ ] Check if "nuts" are in the input 
#  Dovile's comment: See step no.1. There is a variable "allergen". You can enter "nuts" there.
# 4+[ ] Challenge: Check if "seafood" is in the input
#  Dovile's comment: See step no.1. There is a variable "allergen". You can enter "seafood" there.
# 4+[ ] Challenge: Check if "chocolate" is in the input
#  Dovile's comment: See step no.1. There is a variable "allergen". You can enter "chocolate" there.
