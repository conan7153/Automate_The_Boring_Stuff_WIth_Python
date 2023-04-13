#Debugging
'''
As we start to write more complicated program, it is offen challenging to spot the cause of the bug directly from
the source code. Therefore, it is very important for us to learn how to debug our program, such that we can build
our program in a more efficient manner.
'''

#Raise Exception
'''
You can raise your own custom exception in the program using raise statement. The syntax is as follows:
raise Exception()
Just like input(), you can put string into the Exception() to specify the error message when this exception
is raise.
'''
#raise Exception("This is my custom exception.")

'''
If you don't want the exception to crash the program, then you can put this exception as part of try-except clause.
If you still want computer to show the error message when the exception is raised, or you want to store this error 
message for some other usage, then you can 
1, use except Exception as [variable name] to store the Exception Object to a variable
2, use str(Exception Object) to get the error message string.
'''
def fourDividedby(x):
    if x == 0:
        raise Exception("Please don't divide a number using 0.")
    return 4/x
try:
    fourDividedby(0)
except Exception as zeroError:
    print(f"No result come out.\n{zeroError}")

#Trackback
'''
Trackback is an important message that describes you the flow of the program that eventually leads to the bug.
It consists of the following:
1, number of line in the code that causes the bug
2, series of functions calls that evetually reach that line 
3, Error message
'''
'''
def HelloWorld():
    GoodbyeWorld()

def GoodbyeWorld():
    print(4/0)

HelloWorld()
'''

'''
If you want to access this piece of information while avoid crashing the program, you can use traceback module.
traceback.format_exc() method allows you get this traceback error message when you are handling exception
using try-except clause.
'''
import traceback
try:
    def HelloWorld():
        GoodbyeWorld()

    def GoodbyeWorld():
        print(4/0)

    HelloWorld()
except ZeroDivisionError:
    print("The world is not destroyed, why?")
    with open("Trackback.txt", "w") as file:
        file.write(traceback.format_exc())

#Assertion
'''
Assertion is the type of Exception for programmer usage. Its syntax is as follows:
assert [condition], [error message]
An Assertion Exception would be raised if the condition is not met, while nothing will happen
if the condition is met.
Note that Assertion is for testing something that is obviously not acceptable, you should not use
this to handle user behaviour by combine it with try-except clause, you should not use Assertion
as another way of raising Exception because it is possible to turn of python's assertion setting
such that the assertion statement would not be interpreted.
You should only use assert statement for bug detection during development phase, but be mindful that
assertion does not tell you the causes of the bug, it would only tells you that the desired condition
is not met.
'''
age = -1
assert age > 0, "Age cannot be negative number or zero."


