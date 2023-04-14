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
#age = -1
#assert age > 0, "Age cannot be negative number or zero."

#Logging
'''
Beginner programmer sometimes may use print() function to see what are the values stored in some variables as
the program execute, this method is straight forward but not efficient enough for building complicated software.
Python provides similar features with its built-in logging module, and after you finish writing the code, you
can toggle between enable or disable log messages which is ideal for product release and debugging.
logging.debug(Message) same as print() but provides more useful features in combine with other method in logging module
logging.basicConfig(level =, format =) tells python about the format of the logging message for logging.debug()
logging.disable(Message Type) disables the logging functionality in the program, which allows the program to be easily released to the users.
'''
import logging
#logging.disable(logging.DEBUG)
#logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s")
#logging.debug("Hello World")

#Logging Levels
'''
You can categorize log messages into 5 categories, DEBUG, INFO, WARNING, ERROR and CRITICAL(arranged in the sequence
from least important to most important)
You can set the level of the logging message by calling their respective function, such as info(), warning(), error(), critical()
By categorizing messages, you can ask the program to display only logging messages with certain logging level and
above.
Example:
You can do so by setting logging.basicConfig(level = logging.WARNING) to only display logging message with 
WARNING, ERROR and CRITICAL levels.
'''
logging.basicConfig(level = logging.WARNING, format = "%(asctime)s - %(levelname)s - %(message)s", filename = "Logging.txt")
logging.error("This world is fucked up.")
logging.warning("I am not in a good mood today.")
logging.critical("Somebody please destroy this world.")
logging.info("This world is such a nice place to live on.")

#Disable logging
'''
logging.disable() allows you to disable logging message without the need to manually delete or comment out all the
function call in the program. 
By passing a level to the disable() method, all log message with that level or below will be disabled.
Hence, if you want to disable all the logging message, use logging.disable(logging.CRITICAL) to do this.
Note that this function only disable the log messages after it, so you probably want to place it right after 
import logging statement
'''

#Logging to file
'''
logging.basicConfig() method has a 'filename' keyword argument, which allows you to store logging messages externally
in a text file instead of displaying them all on a screen.
'''