# MOD02_1-3.1_Intro_Python.ipynb
# _____________________________________________

# TASK 1
# ____________________
#[ ] increase the number of arguments used in print() to 8 or more 
student_age = 17
student_name = "Hiroto Yamaguchi"
other_student = "Steve"
doviles_arg = "Dovile"
print(student_name,'will be in the class for',student_age, 
      'year old students.','The teacher will be',doviles_arg,'from Python Academy.',
      'The lessons begin at 10 am.','Later another student will join the class and his name is',other_student,'.')

# TASK 2
# _____________________
#[ ] define (def) a simple function called yell_it() and call the function
def yell_it():
    phrase = input ("Enter a phrase:")
    print(phrase.upper(),"!")
#end function
yell_it()

# TASK 3
# _____________________
# [ ] define yell_this() 
def yell_this(str):
    print(str.upper(),"!")
#end function

# [ ] get user input in variable words_to_yell
words_to_yell = input("Enter some words:")

# [ ] call yell_this function with words_to_yell as argument
yell_this(words_to_yell)

# MOD02_1-3.2_Intro_Python.ipynb
# _______________________________________________

# TASK 1
# _______________________
# create and call make_doctor() with full_name argument from user input - then print the return value
def make_doctor(name):
    name = "Doctor " + name
    return name
#end function
    
full_name = input("Enter full name:")

print(make_doctor(full_name))

# TASK 2
# ________________________
# [ ] add a 3rd period parameter to make_schedule
#
print()
print("* Third parameter added")
print()
#

def make_schedule(period1, period2, period3):
    schedule = ("\n[1st] "+ period1.title() + "\n[2nd] " + period2.title() + "\n[3rd] " + period3.title())
    return schedule

student_schedule = make_schedule("mathematics", "history", "science")
print("SCHEDULE:", student_schedule)

#
print()
print("* Schedule for 6 classes [solution no.1]")
print()
#

# [ ] Optional - print a schedule for 6 classes (Tip: perhaps let the function make this easy)
# Solution no.1
def make_schedule_6(p1,p2,p3,p4,p5,p6):
    schedule = ("\n[1st] "+ p1.title() + "\n[2nd] " + p2.title() + "\n[3rd] " + p3.title() + "\n[4th] " + p4.title()
               + "\n[5th] " + p5.title() + "\n[6th] " + p6.title())
    return schedule

student_schedule = make_schedule_6("mathematics", "history", "science", "biology", "chemistry", "geography")
print("SCHEDULE:", student_schedule)

#
print()
print("* Schedule for 6 classes [solution no.2]")
print()
#

def make_schedule_6(p1,p2,p3,p4,p5,p6):
    print("SCHEDULE:")
    print ("[1st]",p1.title(),"\n[2nd]",p2.title(),"\n[3rd]",
           p3.title(),"\n[4th]",p4.title(),"\n[5th]",p5.title(),"\n[6th]",p6.title())
#end function

make_schedule_6("mathematics", "history", "science", "biology", "chemistry", "geography")


# MOD02_1-3.3_Intro_Python.ipynb
# ______________________________________________

# TASK 1
# ____________________________
# [ ] fix the sequence of the code to remove the NameError

def hat_available(color):
    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
    return(color.lower() in hat_colors)

have_hat = hat_available('green')  
  
print('hat available is', have_hat)

# TASK 2
# ____________________________
# [ ] create function bird_available
def bird_available(bird):
    bird_types = 'crow robin parrot eagle sandpiper hawk piegon'
    return (bird.lower()in bird_types.lower())
#end function

# [ ] user input
bird = input("Enter a type bird to search:")

# [ ] call bird_available
have_bird = bird_available(bird)

# [ ] print availbility status
print(bird,"available is",have_bird)

# TASK 3
# _____________________________
# define function how_many
def how_many():
    requested = input("enter how many you want: ")
    return requested

# get the number_needed
number_needed = how_many()
print(number_needed, "will be ordered")

# Practice_MOD02_1-3_IntroPy.ipynb
# __________________________________________________

# TASKS
# _____________________________
# [ ] define and call a function short_rhyme() that prints a 2 line rhyme
def short_rhyme():
    print("First line of rhyme")
    print("Second line of rhyme")
#end function

short_rhyme()

# _______________________________
# [ ] define (def) a simple function: title_it() and call the function
# - has a string parameter: msg
# - prints msg in Title Case

def title_it(msg):
    print(msg.title())
#end function

title_it("hello good morning have a nice day")

# ________________________________
# [ ] get user input with prompt "what is the title?" 
title_name = input("What is the title?")

# [ ] call title_it() using input for the string argument
title_it(title_name)

# ________________________________
# [ ] define title_it_rtn() which returns a titled string instead of printing
def title_it_rtn(msg):
    return msg.title()
#end function

# [ ] call title_it_rtn() using input for the string argumetnt and print the result
print(title_it_rtn(title_name))

# _________________________________
# [ ] create, call and test bookstore() function
def bookstore(book,price):
    return "Title: " + title_it_rtn(book) + ", costs $" + price
#end function    

book_entry = input("Enter title of the book:")
price_entry = input("Enter price of this book:")

print(bookstore(book_entry,price_entry))

# _________________________________
# get name and greeting, send to make_greeting 
def get_name():
    name_entry = input("enter a name: ")
    return name_entry

def get_greeting():
    greeting_entry = input("enter a greeting: ")
    return greeting_entry

def make_greeting(name, greeting = "Hello"):
    return (greeting + " " + name + "!")

print(make_greeting(get_name(), get_greeting()))


# Required_Code_MOD2_IntroPy.ipynb
# _______________________________________________
# [ ] create, call and test fishstore() function 
def fishstore(fish,price):
    return "Fish Type: " + fish + " costs $" + price
#end function    

fish_entry = input("Enter type of fish:")
price_entry = input("Enter price:")

print(fishstore(fish_entry,price_entry))








