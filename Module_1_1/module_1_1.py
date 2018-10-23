# MOD01_1-1.1_Intro_Python.ipynb
# _________________________________________

# TASK 1
# ___________________
# add a comment describing the code purpose
# create an original "Hello World" style message
# _______
# First comment, first "Hello World".
print("Hello World!")

# TASK 2
# ____________________
# Insert a new Code cell below with a comment describing the task
# edit cell: add print() with the message "after edit, save!"
# run the cell
# _______
print("after edit,save!")

# MOD01_1-1.2_Intro_Python.ipynb
# __________________________________________

# TASK 1
# ____________________
# [ ] enter a string in the print() function using single quotes
print('single quote single quote')
# [ ] enter a string in the print() function using double quotes
print("double double double quotes double quotes double quotes")

# TASK 2
# _____________________
# [ ] print an Integer
print(2018)
# [ ] print a strings made of Integer characters
print('2016')

# TASK 3
# _____________________
current_msg = "Run this cell using Ctrl+Enter"
print(current_msg)

# [] run cell above then run this cell after completing the code as directed
print(current_msg)
current_msg = "new current msg dovile"
print(current_msg)

# TASK 4
# _____________________
# [ ] assign a string value to a variable student_name
student_name = "Dovile"
# [ ] print the value of variable student_name
print(student_name)

# [ ] assign the student_name variable  a different string value (a different name)
student_name = "Tamara"
# [ ] print the value of variable student_name
print(student_name)
# [ ] assign a 3rd different string value, to the variable name 
student_name = "Liepa"
# [ ] print the value of variable name
print(student_name)

# [ ] assigning a value to a variable called bucket
bucket = "buk"
# [ ] print the value of bucket 
print(bucket)
# [ ] assign an Integer value (no quotes) to the variable bucket
bucket = 2233
# [ ] print the value of bucket 
print(bucket)

# [ ] print integer 123 number
print(123)
# [ ] print string "123" number
print("123")

# MOD01_1-1.3_Intro_Python.ipynb
# _________________________________________

# TASK 1
# ____________________
# [ ] show the type after assigning bucket = a whole number value such as 16 
bucket = 16
type (bucket)

# [ ] show  the type after assigning bucket = a word in "double quotes"
bucket = "Dovile"
type (bucket)

# [ ] display the type of 'single quoting' (use single quotes) 
type('Sveikas Pasauli')

# [ ] display the type of "double quoting" (use double quotes)
type("Dovile")

# [ ] display the type of "12" (use quotes)
type("12")

# [ ] display the type of 12 (no quotes)
type(12)

# [ ] display the type of -12 (no quotes)
type(-12)

# [ ] display the type of 12.0 (no quotes)
type(12.0)

# [ ] display the type of 1.55
type(1.55)

# [ ] find the type of the type(3) statement (no quotes) - just for fun
type(type(3))

# MOD01_1-1.4_Intro_Python.ipynb
# _________________________________________

# TASK 1
# _____________________
# [ ] add 3 integer numbers
1+2+3

# [ ] add a float number and an integer number
2.4 + 5

# [ ] Add the string "This notebook belongs to " and a string with your first name
"This notebook belongs to " + "Dovile"

# [ ] Create variables sm_number and big_number and assign numbers then add the numbers
sm_number = 3
big_number = 100
sm_number + big_number

# [ ] assign a string value to the variable first_name and add to the string ", remember to save the notebook frequently"
first_name = "Dovile"
first_name + ", remember to save the notebook frequently "

# TASK 2
# _____________________
# [ ] perform string addition in the variable named new_msg (add a string to "my favorite food is ")
new_msg = "My favorite food is " + "bread"
print(new_msg)

# [ ] perform Integer addition in the variable named new_msg (add 2 or more Integers)
new_sum =   0 + 4 + 2 +6
print(new_sum)

# [ ] create and print a new string variable, new_msg_2, that concatenates new_msg + a literal string
new_msg_2 = new_msg + " today"
print(new_msg_2)

# [ ] review and run the code - then fix any Errors
total_cost = 3 + 45
print(total_cost)

# [ ] review and run the code - then fix any Errors
school_num = "123"
print("the street number of Central School is " + school_num)

# [ ] Read and run the code - write a hypothesis for what you observe adding float + int
# [ ] HYPOTHESIS: float + int = float
print(type(3.3))
print(type(3))
print(3.3 + 3)

# TASK 4
# _____________________
# [ ] repair the syntax error 
print('my socks do not match')

# [ ] repair the NameError  
print("my socks match now")

# [ ] repair the syntax error 
print("Save the notebook frequently")

# [ ] repair the NameError 
student_name = "Alton"
print(student_name)

# [ ] repair the TypeError
total = "3"
print(total + " students are signed up for tutoring")

# MOD01_1-1.5_Intro_Python.ipynb
# __________________________________________
# TASK 1
# create the flying bird in character art in the Code cell below
# create # [ ] flying bird character art
print("_         _")
print(" \       /")
print("  \ . . /")
print("     v")

# [ ] capital letter "E" character art
print("**********")
print("**********")
print("****")
print("****")
print("**********")
print("**********")
print("****")
print("****")
print("**********")
print("**********")

# Practice_MOD01_1-1_IntroPy.ipynb
# _________________________________
# [ ] print 'Hello!' and remember to save notebook!
print('Hello!')

print('watch for the cat')

print('Run as a code cell')

# create a code comment that identifies this notebook, containing your name and the date
# Dovile's Notebook. Date: 16th October, 2018

# [ ] print your name
print("Dovile")
# [ ] print "is using Python"
print("is using Python!")

# [ ] create a variable your_name and assign it a sting containing your name
dovile = "Dovile"
#[ ] print your_name
print(dovile)

# [ ] create variables and assign values for: favorite_song, shoe_size, lucky_number
favourite_song = "Sunny Day"
shoe_size = "101"
lucky_number = "12345"
# [ ] print the value of each variable favorite_song, shoe_size, and lucky_number
print(favourite_song)
print(shoe_size)
print(lucky_number)

# [ ] print favorite_song with description
print("My favourite song is " + favourite_song)
# [ ] print shoe_size with description
print("My show size is " + shoe_size)
# [ ] print lucky_number with description
print("My lucky number is " + lucky_number)

# assign favorite_lucky_shoe using
favourite_lucky_shoe = "I know " + lucky_number + " songs " + "and my favourite is number " + shoe_size + " (" + favourite_song + ")"  
print(favourite_lucky_shoe)

# [ ] print a diagonal using "*"
print("        *")
print("      *")
print("    *")
print("  *")
print("*")
print()

# [ ] rectangle using "*"
print("************")
print("**        **")
print("**        **")
print("************")
print()

# [ ] smiley using "*"
print("    *****************")
print("  ****             ***")
print("****                ****")
print("***                   ***")
print("**                      **")
print("**     **        **      **")
print("**          **           **")
print("**   *             *     **")
print("**    *           *     **")
print("**      *********      **")
print(" ***                 ***")
print("  *****          *****")
print("    *****************")

# [ ] display the type of 'your name' (use single quotes)
type('Dovile')

# [ ] display the type of "save your notebook!" (use double quotes)
type("save your notebook!")

# [ ] display the type of "25" (use quotes)
type("25")

# [ ] display the type of "save your notebook " + 'your name'
type("save your notebook" + 'Dovile')

# [ ] display the type of 25 (no quotes)
type(25)

# [ ] display the type of 25 + 10 
type(25+10)

# [ ] display the type of 1.55
type(1.55)

# [ ] display the type of 1.55 + 25
type(1.55 +25)

# assignments ***RUN THIS CELL*** before starting the section
student_name = "Gus"
student_age = 16
student_grade = 3.5
student_id = "ABC-000-000"

# [ ] display the current type of the variable student_name
type(student_name)

# [ ] display the type of student_age
type(student_age)

# [ ] display the type of student_grade
type(student_grade)

# [ ] display the type of student_age + student_grade
type(student_age + student_grade)

# [ ] display the current type of student_id
type(student_id)

# assign new value to student_id 
student_id= "XYZ-111-111"
# [ ] display the current of student_id
print(student_id)

# [ ] create integer variables (x, y, z) and assign them 1-3 digit integers (no decimals - no quotes)
x = 1
y = 10
z = 100

#[ ] insert a code cell below
#[ ] create an integer variable named xyz_sum equal to the sum of x, y, and z
#[ ] print the value of xyz_sum

xyz_sum = x + y + z
print(xyz_sum)

# [ ] fix the error 
print("Hello World!")   

# [ ] fix the error 
print("strings have quotes and variables have names")

# [ ] fix the error 
print( "I have $" + " 5")

# [ ] fix the error 
print('always save the notebook')

#[ ] Display first name or initials as ASCII Art
#[ ] Challenge: insert an additional code cell to make an ASCII picture

# [ ] ASCII ART
print("******          ****       ****")
print("**    **        **  **    ** **")
print("**     **       **   **  **  **")
print("**     **       **     *     **")
print("**    **        **           **")      
print("**   **   ***   **           **  **")
print("*****     ***   **           **  **")

# [ ] ASCII ART
print("        ____")
print("       |    |")
print("      --------")
print("      ( ' < ')")
print("   >-(    0   )-<")
print("    (     0    )")

