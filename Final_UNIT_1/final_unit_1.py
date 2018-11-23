# Required_FINAL_Project_IntroPy.ipynb
# ______________________________________________________________________
# Program: adding_report() function
# This program calls the adding_report() function which repeatedly takes positive integer input until the user quits and then sums the integers and prints a "report".
# The adding_report() function has 1 string parameter which indicates the type of report:
#
# "A" used as the argument to adding_report() results in printing of all of the input integers and the total
# "T" used as the argument results in printing only the total

# The forever (while True) loop diagram
# This diagram represents only part of the assignment - it is the loop and nested if statements inside the function. The code will enter at the while True loop after initializing variables.

# Additional Details
# initialize total variable which will sum integer values entered
# initialize items variable which will build a string of the integer inputs separated with a new line character
# define the adding_report function with one parameter report that will be a string with default of "T"
# inside the function build a forever loop (infinite while loop) and inside the loop complete the following

# use a variable to gather input (integer or "Q")
# check if the input string is a digit (integer) and if it is...
# add input iteger to total
# if report type is "A" add the numeric character(s) to the item string seperated by a new line
# if not a digit, check if the input string is "Q" or starts with a "Q", if "Q" then...
# if the report type is "A" print out all the integer items entered and the sum total
# if report type is "T" then print out the sum total only
# break out of while loop to end the function after printing the report ("A" or "T")
# if not a digit and if not a "Q" then print a message that the "input is invalid"
# Call the adding_report function with "A" and then with "T" report parameters

# Run and test your code before submitting
# [ ] create, call and test the adding_report() function

def adding_report(report = "T"):
    
    total = 0
    items = ""
    
    if report == "T" or report == "A" or report == "":
    
        while True:
            user = input("Integer or Quit: ")
            if user.isdigit():
                total += int(user)
                if report == "A":
                    items += "\n" + str(user)
                else:
                    pass
            elif user.upper().startswith("Q"):
                if report == "A":
                    print("\nItems",items)
                    print("\nTotal","\n" + str(total))
                    break
                else:
                    print ("\nTotal:","\n"+ str(total))
                    break
            else:
                if user != "":
                    print("Invalid input")
                else:
                    pass
#end loop
    else:
        print("Wrong Report type !")
#end function
    
adding_report(input('Choose report type: "A" - all items, "T" - total: '))
#
# _____________________________________________________________________________
#



