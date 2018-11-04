# MOD03_1-5.1_Intro_Python.ipynb
# ________________________________________________

# TASK 1
# _____________________
# Get user input for variable size (S, M, L)
# reply with each shirt size and price (Small =  6,Medium=  7, Large = $ 8)
# if the reply is other than S, M, L, give a message for not available
# optional: add additional sizes

# [ ] code and test SHIRT SALE
size = input("Enter your t-shirt size(XS,S,M,L,XL,XXL):")
if size.isalpha() == False:
    print("Invalid value!")
elif size.upper() == "XS":
    print("size",size.upper(),"costs 5 $")
elif size.upper() == "S":
    print("size",size.upper(),"costs 6 $")
elif size.upper() == "M":
    print("size",size.upper(),"costs 7 $")
elif size.upper() == "L":
    print("size",size.upper(),"costs 8 $")
elif size.upper() == "XL":
    print("size",size.upper(),"costs 9 $")
elif size.upper() == "XXL":
    print("size",size.upper(),"costs 10 $")    
else:
    print(size.upper()," is not available")

# TASK 2
# _____________________
str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# [ ] Add the 3 numbers as integers and print the result
result = int(str_num_1) + int(str_num_2) + int_num_3
print("Result = ",result)
# _____________________
str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# [ ] Add the 3 numbers as test strings and print the result
result_str = str_num_1 + str_num_2 + str(int_num_3)
print("Result str = ",result_str)
# _____________________
# [ ] initialize str_integer variable to a string containing characters of an integer (quotes)
# [ ] initialize int_number variable with an integer value (no quotes)
# [ ] initialize number_total variable and add int_number + str_integer using int casting
# [ ] print the sum (number_total)

# [ ] code and test: adding using int casting
str_integer = "24"
int_number = 20
number_total = int(str_integer) + int_number
print(number_total)
# ______________________

# TASK 3
# ______________________
# get input of 2 integer numbers
# cast the input and print the input followed by the result
# Output Example: 9 + 13 = 22
# Optional: check if input .isdigit() before trying integer addition to avoid errors in casting invalid inputs

# [ ] code and test the adding calculator
num_1 = input("First number:")
if num_1.isdigit() == True:
    num_2 = input("Second number:")
    if num_2.isdigit() == True:    
        sum = int(num_1) + int(num_2)
        print(num_1,"+",num_2,"=",sum)
    else:
        print("Invalid second number")
else:
    print("Invalid first number")

# MOD03_1-5.2_Intro_Python.ipynb
# ________________________________________________

# TASK 1
# _____________________
# [ ] print the result of subtracting 15 from 43
print("43 - 15 =",43-15)

# [ ] print the result of multiplying 15 and 43
print("15 * 43 =",15*43)

# [ ] print the result of dividing 156 by 12
print("156 / 12 =",156/12)

# [ ] print the result of dividing 21 by 0.5
print("21 / 0.5 =",21/0.5)

# [ ] print the result of adding 111 plus 84 and then subtracting 45
print("(111 + 84) - 45 =",(111+84)-45)

# [ ] print the result of adding 21 and 4 and then multiplying that sum by 4
print("(21 + 4)*4 =",(21+4)*4)

# TASK 2
# _____________________
# define function multiply(), and within the function:
# gets user input() of 2 strings made of whole numbers
# cast the input to int()
# multiply the integers and return the equation with result as a str()
# return example
# 9 * 13 = 117

# [ ] create and test multiply() function
def multiply():
    numb_str_1 = input("First number: ")
    numb_str_2 = input("Second number: ")
    result = numb_str_1 + "*" + numb_str_2 + "=" + str(int(numb_str_1)*int(numb_str_2))    
    return result
#end function

multiply()

# TASK 3
# _____________________
# update the multiply() function to multiply or divide
# single parameter is operator with arguments of * or / operator
# default operator is "*" (multiply)
# return the result of multiplication or division
# if operator other than "*" or "/" then return "Invalid Operator"

# [ ] create improved multiply() function and test with /, no argument, and an invalid operator ($)
def multiply(operator = "*"):
    if operator == "*":
        numb_1 = int(input("First number: "))
        numb_2 = int(input("Second number: "))
        result = str(numb_1) + operator + str(numb_2) + "=" + str(int(numb_1)*int(numb_2))    
        return result
    elif operator == "/":
        numb_1 = int(input("First number: "))
        numb_2 = int(input("Second number: "))
        result = str(numb_1) + operator + str(numb_2) + "=" + str(int(numb_1)/int(numb_2))    
        return result
    else:
        return "Invalid operator!"
#end function

print(multiply("/"))
print()
print(multiply())
print()
print(multiply("$"))

# TASK 4
# ______________________
# Review, run, fix 
student_name = input("enter name: ").capitalize()
if student_name.startswith("F"):
    print(student_name,"Congratulations, names starting with 'F' get to go first today!")
elif student_name.startswith("G"):
    print(student_name,"Congratulations, names starting with 'G' get to go second today!")
else:
    print(student_name, "please wait for students with names starting with 'F' and 'G' to go first today.")

# ______________________

# Practice_MOD03_1-5_IntroPy.ipynb
# _______________________________________________

# TASKS
# ______________________
# [ ] complete rainbow colors
color = input("Enter your favourite color first letter (ROYGBIV):").upper()

if color == "R":
    print("RED")
elif color == "O":
    print("ORANGE")
elif color == "Y":
    print("YELLOW")
elif color == "G":
    print("GREEN")
elif color == "B":
    print("BLUE")
elif color == "I":
    print("INDIGO")
elif color == "V":
    print("VIOLET")
else:
    print("No match")

# ________________________
# [ ] make the code above into a function rainbow_color() that has a string parameter, 
# get input and call the function and return the matching color as a string or "no match" message.
# Call the function and print the return string.

def rainbow_color(color):
    color = color.upper()
    if color == "R":
        return "RED"
    elif color == "O":
        return "ORANGE"
    elif color == "Y":
        return "YELLOW"
    elif color == "G":
        return "GREEN"
    elif color == "B":
        return "BLUE"
    elif color == "I":
        return "INDIGO"
    elif color == "V":
        return "VIOLET"
    else:
        return "No match"
# end function

fav_color = input("Enter your favourite color first letter (ROYGBIV)")
print(rainbow_color(fav_color))

# _________________________
# [ ] complete age_20()
def age_20(age):
        if age > 20:
            return age - 20
        elif age < 20:
            return age + 20
        else: 
            return  0
# end function   

age = int(input("Enter your age: "))
print(str(age_20(age)) + " years old, 20 years difference from now")    
    
# _________________________
# [ ]  create rainbow_or_age()
def rainbow_or_age(str):
    if str.isdigit() == True:
        return age_20(int(str))
    elif str.isalpha() == True:
        return rainbow_color(str)
    else:
        return False
# end function

print(rainbow_or_age("R"))
print()
print(rainbow_or_age("25"))
print()
print(rainbow_or_age("Abc111"))
# __________________________
# [ ]  add 2 numbers from input using a cast to integer and display the answer 
num_1 = input("First number: ")
num_2 = input("Second number: ")
int(num_1)+ int(num_2)
# ___________________________
# [ ] Multiply 2 numbers from input using cast and save the answer as part of a string "the answer is..."
# display the string using print
num_1 = input("First number: ")
num_2 = input("Second number: ")
print("the answer is ...",int(num_1)*int(num_2))
# ____________________________
# [ ] get input of 2 numbers and display the average: (num1 + num2) divided by 2
num_1 = input("First number: ")
num_2 = input("Second number: ")
(int(num_1)+int(num_2))/2

# ____________________________
# [ ] get input of 2 numbers and subtract the largest from the smallest (use an if statement to see which is larger)
# show the answer
num_1 = int(input("First number: "))
num_2 = int(input("Second number: "))
if num_1 > num_2:
    print(num_1 - num_2)
elif num_2 > num_1:
    print(num_2 - num_1)
else:
    print(0)

# ______________________________
# [ ] Divide a larger number by a smaller number and print the integer part of the result
# don't divide by zero! if a zero is input make the result zero
# [ ] cast the answer to an integer to cut off the decimals and print the result
num_1 = input("First number: ")
num_2 = input("Second number: ")
if (num_1.isdigit() == True) and (num_2.isdigit() == True):
    num_1 = int(num_1)
    num_2 = int(num_2)
    if num_1 == 0:
        print("can't devide by zero ! Result is",0)
    elif num_2 == 0:
        print("can't devide by zero ! Result is",0)
    elif num_1 > num_2:
        print(int(num_1/num_2))
    elif num_2 > num_1:
        print(int(num_2/num_1))
    else:
        print(1)
else:
    print("Invalid Value!")

# ________________________

# Required_Code_MOD3_IntroPy.ipynb
# ______________________________________________
# Program: Cheese Order
# set values for maximum and minimum order variables
# set value for price variable
# get order_amount input and cast to a number
# check order_amount and give message checking against
# over maximum
# under minimum
# else within maximum and minimum give message with calculated price
# Sample input and output:
#
# Enter cheese order weight (numeric value): 113
# 113.0 is more than currently available stock
# Enter cheese order weight (numeric value): .15
# 0.15 is below minimum order amount
# Enter cheese order weight (numeric value): 2
# 2.0 costs $15.98

# [ ] create, call and test 
min_order = 1
max_order = 50
price = 1.5

order_amount = float(input("Enter cheese order weight (numeric value):"))
if order_amount < min_order:
    print(order_amount,"is below minimum order amount")
elif order_amount > max_order:
    print(order_amount,"is more than currently available stock")
else:
    result = price*order_amount
    print(order_amount,"costs $",result)
    
# _______________________    


