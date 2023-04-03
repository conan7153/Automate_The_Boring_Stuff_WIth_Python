#Functions
'''
The purpose of using functions is to avoid duplicating code and make your code
easier to read & maintain.
'''

def sayHello(name):
    print("Hello" + str(name))

sayHello("Alice")
sayHello("Bob")

#Return Value & Return Statements
'''
Function call evalute to a value that can be passed to a variable 
Return statement specifies the value that a function should return when that function call ends
'''

def addition(a, b):
    result = a + b
    return result

x = addition(2, 3)
print(x)

'''
Since function call can be evaluated down to a value, you can pass function as a argument of another function
'''

def multiplication(a, b):
    result = a * b
    return result

y = multiplication(10, addition(3, 7))

#NoneType Value
'''
Python has keyword value None to represent the absence of a value.
It is returned by a function call if that function does not actually return a value.
For example, if the function does not have return statement or just having a return keyword without any values behind
'''
a = print("Hello World")
print(a)

#Keyword Argument(Optional Argument)
'''
Instead of providing arguments in sequence, you can assign values to arguments by keyword if you
declare those argument as keyword arguments(optional arguments)
After declare them, it is optional to explictly write them in a function call, and the default value
used in the define statement would be regarded as the assigned value of that keyword argument.
Note that if you are mixing keyword arguments and normal arguments, you need to define function in below way:
def function(normal arguments, keyword arguments)
'''
def greetUser(userName, greetingWord = "Hello"):
    print(greetingWord + " " + userName)

greetUser("Alice")
greetUser("Have a nice day", "Bob")
greetUser("Charlie", greetingWord = "Nice weather")

#Global & Local Scopes
'''
Variables created in global scopes are global variables, they can accessed anywhere within the program.
Variables created in local scopes are local variables, they can only be accessed within that local scope.
(For example, local variable created in a function can only be accessed within the function itself)
In general,
if there are global & local variable with the same name. Then within that local scope, the name would refer
to the local variable.
In such cases, if you want to refer to the global variable of that name, you can use global keyword to declare
that variable to be the global one.
'''
hello = "Global"
def Alice():
    hello = "Alice_Local"
    print(hello)      #Result should be "Alice_Local"

def Bob():
    hello = "Bob_Local"
    print(hello)     #Bob_Local
    Alice()          #Alice_Local

def Charlie():
    global hello
    hello = "From Charlie, hello is still global"
print(hello)
Charlie()
print(hello)

#Exception Handling
'''
To prevent any possible error from crashing the program, exception handling would be needed.
For python, exception handling is carried out in a try-except code block.
The code that may potentially cause error is put in try block
while code that needs to be run when errors happen is put in except block.

Note: after error happens, the execution of code would immediately jump to except block,
any other code in try block after that error would not be executed.
'''
def division(x):
    result = 42 / x
    return result

try:
    division(0)
except ZeroDivisionError:
    print("You can't divide numbers by 0!")



