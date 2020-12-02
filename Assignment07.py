# ------------------------------------------------- #
# Title: Assignment07
# Description: Demo of exception handling
# using custom error classes and pickling
# ChangeLog: (Who, When, What)
# KSanchez,11.30.2020,Created Script
# ------------------------------------------------- #

# --------------Exception Handling----------------- #

----- Try-Except:
try:  # Tests the following code block for errors
    x = int(input("Please enter a number: "))
    y = int(input("Please enter a second number: "))
    add = x + y
    subtract = x - y
    divide = x/y

except ZeroDivisionError as e:  # Handles a ZeroDivisionError if user enter 0 for y
    print("Variable y cannot be a zero.")
    print("Built-in Python error info:")
    print(e, e.__doc__, type(e), sep='\n')
except ValueError as e:  # Handles a ValueError if user input is a string or space/enter key
    print("Please enter an integer.")
    print("Built-in Python error info:")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:  # Handles all other error types and provides details
    print("Something else went wrong.")
    print("Built-in Python error info:")
    print(e, e.__doc__, type(e), sep='\n')

# ----- Else:
try:  # Tests the following code block for errors
    x = int(input("Please enter a number: "))
    y = int(input("Please enter a second number: "))
    add = x + y
    subtract = x - y
    divide = x/y

except Exception as e:  # Handles all error types and provides details
    print("Something else went wrong.")
    print("Built-in Python error info:")
    print(e, e.__doc__, type(e), sep='\n')
else:  # Displays results and message if user input does not generate an error
    print("Added: ", add)
    print("Subtracted: ", subtract)
    print("Divided: ", divide)
    print("No errors occurred.")

# ----- Pass and Finally:
try:  # Tests the following code block for errors
    x = int(input("Please enter a number: "))
    y = int(input("Please enter a second number: "))
    add = x + y
    subtract = x - y
    divide = x/y

except Exception as e:  # Handles all error types and provides details, but continues program
    print("Display error message, but ignore and move on through program.")
    print("Built-in Python error info:")
    print(e, e.__doc__, type(e), sep='\n')
    pass # Tells program to ignore error and continue through program
finally:  # Performs actions after all try-except actions
    print("This exception test is complete.")

# The program reaches this block, even if errors occur
print("Added: ", add)
print("Subtracted: ", subtract)
print("Divided: ", divide)

# ----- Handling a file:
try:
    objFile = open("file.txt", "wb")
    objFile.write("Test") # Generates a TypeError because a bytes-like object is required
except Exception as e:
    print("Unable to write to the file.")
    print("Built-in Python error info:")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    objFile.close()  # Closes the file object and continues the program

# ----- Raising an Error:
x = int(input("Please enter a number: "))

if x < 0:  # Raises an error if the user enters a negative number
    raise ValueError("Please enter a number greater than zero.")
elif x == 0:  # Raises an error if the user enters a zero
    raise ZeroDivisionError("Please do not enter a zero.")

# -------------------Pickling---------------------- #

# ----- Writing to a File:
import pickle
pickleDict = {}

pickleDict["Onigiri"] = ["salted salmon", "umeboshi", "tuna mayo"]
pickleDict["Ramen"] = ["shoyu", "tonkotsu", "miso"]

with open('dataPick.pkl', 'wb') as pickleFile: # Opens a file for writing binary data and specifies the binary object
    pickle.dump(pickleDict, pickleFile) # Writes data to new file specifying data and file object

# ----- Reading a File:

with open('dataPick.pkl', 'rb') as pickleFile:  # Opens a file for reading binary data
    newData = pickle.load(pickleFile) # Loads data from file object and stores
    print(newData)  # Prints all the loaded data
