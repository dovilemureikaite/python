# MOD04_1-7.1_Intro_Python.ipynb
# ______________________________________________________________________
#
# TASK 1
# ____________________________________
# [ ] Program: Get a name forever ...or until done
# create variable, familar_name, and assign it an empty string ("")
# use while True:
# ask for user input for familar_name (common name friends/family use)
# keep asking until given a non-blank/non-space alphabetical name is received (Hint: Boolean string test)
# break loop and print a greeting using familar_name

# [ ] create Get Name program
familiar_name = ""

while True:
    familiar_name = input("Enter name: ")
    if familiar_name.isalpha():
        break
    else:
        print("Wrong name ! ")
#end while loops

print(familiar_name, "congratulations !")
# ___________________________________

# TASK 2
# ___________________________________
# Program: Shirt Count
# enter a sizes (S, M, L)
# tally the count of each size
# input "exit" when finished
# report out the purchase of each shirt size

# [ ] Create the Shirt Count program, run tests
count_s = 0
count_m = 0
count_l = 0

while True:
    size = input('Enter shirt size (S,M,L) or "exit" (to finish): ')
    if size.lower().startswith("e"):
        print()
        break
    elif size.upper() == "S":
        count_s += 1
    elif size.upper() == "M":
        count_m += 1
    elif size.upper() == "L":
        count_l += 1
    else:
        print("Wrong Value entered !")
        
#end loop

print("Your purchases:")
print("Shirt S =",count_s)
print("Shirt M =",count_m)
print("Shirt L =",count_l)
# __________________________________

# CHALLENGE: Shirt Register (optional)
# Update the Shirt Count program to calculate cost
# 
# use shirt cost (S = 6, M = 7, L = 8)
# to calculate and report the subtotal cost for each size
# to calculate and report the total cost of all shirts

# [ ] Create the Shirt Register program, run tests

count_s = 0
count_m = 0
count_l = 0

cost_s = 0
cost_m = 0
cost_l = 0

total_cost = 0

while True:
    size = input('Enter shirt size (S,M,L) or "exit" (to finish): ')
    if size.lower().startswith("e"):
        print()
        break
    elif size.upper() == "S":
        count_s += 1
        cost_s = count_s * 6
    elif size.upper() == "M":
        count_m += 1
        cost_m = count_m * 7
    elif size.upper() == "L":
        count_l += 1
        cost_l = count_l * 8
    else:
        print("Wrong Value entered !")
    total_cost = cost_s + cost_m + cost_l
#end loop

print("Your purchases:")
print("Shirt S =",count_s,",subtotal =",cost_s)
print("Shirt M =",count_m,",subtotal =",cost_m)
print("Shirt L =",count_l,",subtotal =",cost_l)
print("Total cost = ",total_cost)
# ____________________________________________

# MOD04_1-7.2_Intro_Python.ipynb
# __________________________________________________________________

# TASK 1
# ________________________________
# Program: Animal Names
# Use while to get the user input, animal_name, of 4 animals
# use a counter, num_animals, in the while loop condition
# append the names to a string variable, all_animals
# User can exit early by typing "exit" (check if animal_name is "exit" and break)
# when the loop finishes, print the names of all_animals
# -bonus: print "no animals" if animal_name is empty after exiting the loop
# Tip: Think about Sequence and variables that need to be initialized before the while loop

# [ ] Create the Animal Names program, run tests

num_animals = 0
all_animals = ""

while num_animals < 4:
    animal_name = input('Enter animal name ("exit" to finish) : ').lower()
    if animal_name == "exit":
        break
    elif animal_name == "":
        num_animals += 1 #used as a counter
    elif animal_name == " ":
        break
    else:
        num_animals += 1
        all_animals += animal_name + "\t"
# end loop
if all_animals:
    print(all_animals)
elif animal_name == " ":
    print("No space allowed")
else:
    print("No animals")
# _________________________________
#
# TASK 2
# _________________________________

# Program: Long Number
# Create variables
# int_num and get user input string of only digits
# long_num and initialize it as an empty string
# Create a while loop that runs as long as the input is all digits
# Inside the while loop
# add int_num to the end of long_num
# get user input for int_num again (inside while loop this time)
# After the loop exits
# print the value of long_num

# [ ] Create the program, run tests
long_num = ""

int_num = input("Enter a number: ")

while int_num.isdigit() == True:
    long_num += int_num
    int_num = input("Enter a number: ")
#end loop

print()
print(long_num)
# _________________________________

# TASK 3
# _________________________________
# Fix the Errors
# This loop never runs
#
# This is a logic error - there is no ErrorMessage, but the code doesn't work

# [ ] review the code, run, fix the Logic error
count = 1

# loop 5 times
while count < 6:
    print(count, "x", count, "=", count*count)
    count +=1
    
# _________________________________
#
#
# Practice_MOD04_1-7_IntroPy.ipynb
# ___________________________________________________________________________
#
# [ ] use a "forever" while loop to get user input of integers to add to sum, 
# until a non-digit is entered, then break the loop and print sum
sum = 0
while True:
    num = input ("Enter a number: ")
    if num.isdigit() == True:
        sum += int(num)
    else:
        break
#end loop

print("Sum:",sum)
#
# ________________________________
#
# use a while True loop (forever loop) to give 4 chances for input of a correct color in a rainbow",
# rainbow = "red orange yellow green blue indigo violet"

rainbow = "red orange yellow green blue indigo violet"
count = 0

while True:
    color = input("Enter color: ")
    if color.lower() in rainbow:
        print(color,"is in the rainbow")
        break
    else:
        count += 1
        if count > 3:
            print("No more tries")
            break         
#end loop
#
# _______________________________
#
# [ ] Get input for a book title, keep looping while input is Not in title format (title is every word capitalized)
title = ""
while title.istitle() == False:
    title = input("Enter a book title: ")
#end loop
print()
print("Result: ",title)
#
# ________________________________
#
# 
# [ ] create a math quiz question and ask for the solution until the input is correct
result = 24
guess = int(input("4 * 6 = "))

while guess != result:
    guess = int(input("4 * 6 = "))
#end loop

print("____________")
print("4 * 6 = ", guess)


# _______________________________
#
# [ ] review the code, run, fix the error
tickets = int(input("enter tickets remaining (0 to quit): "))

while tickets > 0:
        # if tickets are multiple of 3 then "winner"
    if int(tickets/3) == tickets/3:
        print("you win!")
    else:
        print("sorry, not a winner.")
    tickets = int(input("enter tickets remaining (0 to quit): "))

print("Game ended")
    
# _______________________________
#
# create a function: quiz_item() that asks a question and tests if input is correct
# uiz_item()has 2 parameter strings: question and solution
# shows question, gets answer input
# returns True if answer == solution or continues to ask question until correct answer is provided
# use a while loop
# create 2 or more quiz questions that call quiz_item()
# Hint: provide multiple choice or T/F answers
# Create quiz_item() and 2 or more quiz questions that call quiz_item()
def quiz_item(question,solution):
    print(question)
    answer = input("Enter answer: ")
    
    while answer != solution:
        answer = input("Enter answer: ")
    
    return True

#end function

print(quiz_item("2 * 2 = ", "4"))
print()
print(quiz_item("3 * 4 = ", "12"))
#
# _______________________________
#
# Required_Code_MOD4_IntroPy.ipynb
# __________________________________________________________________________
#
# Program: str_analysis() Function
# Create the str_analysis() function that takes 1 string argument and returns a string message. The message will be an analysis of a test string that is passed as an argument to str_analysis(). The function should respond with messages such as:

# "big number"
# "small number"
# "all alphabetic"
# "multiple character types"
# The program will call str_analysis() with a string argument from input collected within a while loop. The while loop will test if input is empty (an empty string "") and continue to loop and gather input until the user submits at least 1 character (input cannot be empty).

# The program then calls the str_analysis() function and prints the return message.

# Sample input and output:
# enter nothing (twice) then enter a word

# enter word or integer: 
# enter word or integer: 
# enter word or integer: Hello
# "Hello" is all alphabetical characters!
# alphabetical word input

# enter word or integer: carbonization
# "carbonization" is all alphabetical characters!
# numeric inputs

# enter word or integer: 30
# 30 is a smaller number than expected

# enter word or integer: 1024
# 1024 is a pretty big number
# loop until non-empty input is submitted
# This diagram represents the input part of the assignment - it is the loop to keep prompting the user for input until they submit some input (non-empty).

# Once the user gives input with characters use the input in calling the str_analysis() function.

# Additional Details
# In the body of the str_analysis() function:

# Check if string is digits
# if digits: convert to int and check if greater than 99
# if greater than 99 print a message about a "big number"
# if not greater than 99 print message about "small number"
# check if string isalpha then (since not digits)
# if isalpha print message about being all alpha
# if not isalpha print a message about being neither all alpha nor all digit
# call the function with a string from user input

# Run and test your code before submitting

# [ ] create, call and test the str_analysis() function  

def str_analysis(user_str):         
    if user_str.isdigit():
        if int(user_str) > 99:
            print("\n",user_str,"is a BIG number")
        else: 
            print("\n",user_str,"is a SMALL number")
    else:
        if user_str.isalpha():
            print("\n",user_str,"\n\nAll Alphabetic")
        else:
            print("\nMultiple character types (neither all alpha nor all digit)")  
#end function   

usr_str = ""
while True:
    if usr_str == "":
        usr_str = input ("enter word or integer: ")
    else:
        str_analysis(usr_str)
        break        
#end loop

# __________________________________________________________________________
#