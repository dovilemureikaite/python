# MOD03_1-4.1_Intro_Python.ipynb
# _______________________________________________
# TASK 1
# ______________________
sunny_today = True
# [ ] test if it is sunny_today and give proper responses using if and else
if sunny_today:
    print("Today is sunny day!")
else:
    print("More clouds today")
        
# _______________________
sunny_today = False
# [ ] use code you created above and test sunny_today = False
if sunny_today:
    print("Today is sunny day!")
else:
    print("More clouds today")

# TASK 2
# ______________________
test_string_1 = "welcome"
test_string_2 = "I have $3"
# [ ] use if, else to test for islower() for the 2 strings

print("* String '",test_string_1,"' evaluation:")
print()

if test_string_1.islower():
    print("String is all lower case")
else:
    print("Seems there are upper case letters in the string")

# another if
print()
print("* String '",test_string_2,"' evaluation:")
print()

if test_string_2.islower():
    print("String is all lower case")
else:
    print("Seems there are upper case letters in the string ")

# _________________________
test_string_1 = "welcome"
test_string_2 = "I have $3"
test_string_3 = "With a function it's efficient to repeat code"
# [ ] create a function w_start_test() use if & else to test with startswith('w')
def w_start_test(test_string):
    if test_string.lower().startswith("w"):
        print("String '",test_string,"' starts with 'w'")
    else:
        print("String '",test_string,"' does NOT start with 'w'")
    
# [ ] Test the 3 string variables provided by calling w_start_test()
w_start_test(test_string_1)
w_start_test(test_string_2)
w_start_test(test_string_3)

# MOD03_1-4.2_Intro_Python.ipynb
# ________________________________________________

# TASK 1
# _____________________
x = 9 + 4
# [ ] create a test to print() True or False for x is equal to 13
print(x == 13)
# _____________________
# [ ] create a test to print True or False for 3 + 3 is greater than 2 + 4
print((3 + 3) > (2 + 4))

# TASK 2
# _____________________
# [ ] create an if/else statement that tests if y is greater than or equal x + x 
# [ ] print output: "y greater than or equal x + x is" True/False ...or a similar output
x = 3
y = x + 8

if y >= x + x:
    print("y greater than or equal x + x is True")
else:
    print("y greater or equal x + x is False")


# MOD03_1-4.3_Intro_Python.ipynb
# ___________________________________________________

# TASK 1
# ______________________
msg = "Hello"
# [ ] print the True/False results of testing if msg string equals "Hello" string
print(msg == "Hello")
# ______________________
greeting = "Hello"
# [ ] get input for variable named msg, and ask user to 'Say "Hello"'
# [ ] print the results of testing if msg string equals greeting string
msg = input('Say "Hello": ')
print("msg == greeting:",msg == greeting)

# TASK 2
# ______________________
# [ ] get input for a variable, answer, and ask user 'What is 8 + 13? : '
# [ ] print messages for correct answer "21" or incorrect answer using if/else
# note: input returns a "string"

answer = input("What is 8 + 13? :")
correct = "21"

if answer == correct:
    print("You are right!, correct answer is 21")
else:
    print("Try again !")

# TASK 3
# ______________________
# [ ] Create the program, run tests
def tf_quiz(question,correct_ans):
    user_ans = input("(T/F) " + question)
    if user_ans == correct_ans:
        return "correct"
    else: 
        return "incorrect"
#end function

# no.1
result = tf_quiz("Water is blue? ","F")
print("Your answer is",result)
# no.2
result = tf_quiz("Tokyo is the capital of Japan? ","T")
print("Your answer is",result)
# no.3
result = tf_quiz("Python is the longest snake? ","T")
print("Your answer is",result)

# 
# Practice_MOD03_1-4_IntroPy.ipynb
# __________________________________________________
# # [ ] input avariable: age as digit and cast to int
# if age greater than or equal to 12 then print message on age in 10 years 
# or else print message "It is good to be" age

age = int(input("enter age:"))

if age >= 12:
    print(age,"+ 10 years =",age + 10)
else:
    print("It is good to be",age)
# _______________________
# [ ] input a number 
# if number IS a digit string then cast to int
# print number "greater than 100 is" True/False
# if number is NOT a digit string then message the user that "only int is accepted"

number = input("Enter a number: ")

if number.isdigit():
    number = int(number)
    print("greater than 100 is",number > 100)
else:
    print("only int is accepted")
# _________________________
# [ ] create check_guess()
# call with test
def check_guess(letter,guess):
    if guess.isalpha():
        if guess == letter:
            print("Correct")
            return True
        else:
            if guess < letter:
                print("low")
                return False
            else:
                print("high")
                return False
    else:
        print("Invalid")
        return False
#end function

result = check_guess("R","R")
print("Your answer is",result)
# __________________________
# [ ] call check_guess with user input

guess = input("Guess a letter: ")
result = check_guess("R",guess)
print("Your answer is",result)
# ___________________________
# [ ] create letter_guess() function, call the function to test
def letter_guess(answer_letter):
    user_letter = input("Enter a letter:")
    result = check_guess(answer_letter,user_letter)
    if result:
        return True
    else:
        user_letter = input("Enter a letter:")
        result = check_guess(answer_letter,user_letter)
        if result:
            return True
        else:
            user_letter = input("Enter a letter:")
            result = check_guess(answer_letter,user_letter)
            if result:
                return True
            else:
                return False
#end function

print(letter_guess("K"))
# _____________________________
# [ ] complete pet conversation
question = "What pet(s) do you have?" #example "cat and dog", "cat", "dog"
about_pet = input(question).lower()

if "dog" in about_pet:
    if ("cat" in about_pet) == False:
        print("Ah, you have a dog!")
        question = "What is the name of your dog?"
        about_pet = input(question).lower()
        print ("Beautifull name. Thanks")

if "cat" in about_pet:
    if ("dog" in about_pet) == False:
        print("You have a cat")
        question = "What is the name of your cat?"
        about_pet = input(question).lower()
        print ("Cute name. Thank you")
        
    if "dog" in about_pet:
        print("2 animals in the house.")
        question = "Who is the boss ?"
        about_pet = input(question).lower()
        if "cat" in about_pet:
            print("Cats are smart, they know how win and become a boss")
            print("Thank you for the answer")
        if "dog" in about_pet:
            print("Dog is a friendly boss") 
            print("Thanks for the answer")
# ___________________________________
