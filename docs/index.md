# Exception Handling and Pickling
KSanchez, 12.1.2020

## Introduction
This week, I created a program that demonstrates exception handling and pickling. 
This assignment included new components such as using the try, except, else, pass and finally blocks as well as the pickle module.

## Researching the Program
In addition to reviewing the module notes provided by the instructor, Randal Root, 
I began by researching the topics I would need to incorporate within this program, starting with exception handling and then moving on to pickling.

### Exception Handling in Python
My first task was to research exception handling in Python, and I found a few good sources of information. 

#### W3Schools

The first source was from a site that many of the course links came from, w3schools.com. The site explained the Python try block which “let’s you test a block of code for errors,” the except block which “lets you handle the error,” and the finally block which “ lets you execute code, regardless of the result of the try- and except blocks.” (w3schools, https://www.w3schools.com/python/python_try_except.asp, 2020) (External Site).  
The site went on to explain that when errors (or exceptions) occur, Python normally stops and generates an error message. Using a try statement will raise an error that can execute one or many except blocks. Using the else keyword “[defines] a block of code to be executed if no errors were raised.” And using a finally block “will be executed regardless if the try block raises an error or not” which “can be useful to close objects and clean up resources.”
Raising an exception was the last topic covered on this page. Using the raise keyword will throw (or raise) an exception, which can help with handling specific types of errors.

#### YouTube – Trevor Payne
The second source I found was also from a page previously included in the course links, a YouTube video by Trevor Payne. The video was called “Let's Learn Python - Basics #5 of 8 - Exception Handling” and focused on using exception handling to prevent scripts from breaking due to user input. (YouTube, https://www.youtube.com/watch?v=hrR0WrQMhSs&list=PL82YdDfxhWsDJTq5f0Ae7M7yGcA26wevJ&index=5, 2020) (External Site).
Trevor Payne explains the try statement as trying to execute code and the except statement as catching all or just specific errors. He does a great job of explaining how exception handling helps to catch multiple types of errors while displaying messages that can be helpful for end users or with debugging.
Another keyword he covers is pass, which signals to the program to ignore and move on. This keyword has been covered in previous modules and can be used in for and while loops as well as within try/except blocks. Trevor also covered using the raise keyword which he noted is used to force a specific error or exception to be called.
The last keyword he covers is finally, which is a block with the last actions to perform after try-except. This block always happens at the end and occurs before any real errors are returned.

#### The Python Standard Library

The last source I reviewed was the Built-In Exceptions page in the Python Standard Library. (Python Standard Library, https://docs.python.org/3/library/exceptions.html#bltin-exceptions, 2020) (External Site). 
It describes exceptions in high-level terms, but lists all built-in exceptions that can be used for specific error handling.(Figure 1).

## Summary
