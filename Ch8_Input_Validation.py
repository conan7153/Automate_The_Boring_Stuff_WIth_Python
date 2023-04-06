#Input Validation
'''
When you are writing actual program for intented users, you need to ensure the users enter the type of data
that you want them to type in, else error or bugs may be introduced into the system and end up crashing the
program.
You can use basic python knowledge to write input validation function to check user input, however, this may
get tedious if you are getting plenty of user input, and you may miss certain conditions if the input you want
to validate has complicated logic.
This chapter uses python module "pyinputplus" to do these jobs in much simpler ways.
'''
import pyinputplus as pyip

#Useful pyinputplus functions
'''
inputStr()         Ordinary function that shares pyinputplus features
inputNum()         ensures user enters number, and return the valid input
inputInt()         ensures integer input
inputFloat()       ensures float input
inputChoice()      ensures user enters one of the provided choices
inputMenu()        similar to inputChoice() but shows choice in list
inputDatetime()    ensures user enters a data and time
inputYesNo()       ensures user enters a "yes" or "no" response
inputBool()        ensures user enters a boolean value
inputEmail()       ensures user enters a valid email address
inputFilePath()    ensures user enters a valid filepath/filename, optionally can check whether that file exists
inputPassword()    same as input, but displays * when user types so as to protect privacy

Just like input(), you can pass a string as the argument to pop a prompt to the user.
'''
userInput = pyip.inputNum("Please enter a number: ")
print(f"You have entered {userInput}.")

#Specifying range of accepted numerical values for numerical value validation
'''
For numerical validation function like inputNum(), inputInt(), inputFloat() etc.
You can specify range of accepted values using min, max, greaterThan, lessThan keyword arguments
'''
userInput = pyip.inputInt("Enter your age if you want to buy alcohol: ", min = 18)
print(f"Your age is {userInput}. Alright you can buy alcohol.")

#Allow blank input for user
'''
You can use blank keyword argument to specify whether a input accepts blank input,
which basically allows users to not enter anything at all.
'''
userInput = pyip.inputStr("You have any interesting to share about yourself?", blank = True)
if userInput == "":
    print("Alright, it is ok if you don't want to share anything.")

#Restrict user input attempt
'''
If you want to restrict user input attempt for quiz ,security purpose etc, you can use "limit" or "timeout"
keyword argument to specify the number of attempts or time limit that pyinputplus can accept before rejecting
any further input from the users.
If user exceeds maximum attempts, RetryLimitException would be raised
If user exceeds time limit, TimeoutException would be raised
'''
try:
    password = pyip.inputPassword("Please enter your bank account password: ", limit = 3)
except pyip.RetryLimitException:
    print("Too many failed attempts, your account has been frozen.")

try:
    answer = pyip.inputMenu(["West", "East", "North", "South"], prompt = "Guess where do I live?", lettered = True, timeout = 5)
except pyip.TimeoutException:
    print("Time out! I am not gonna let your answer anymore.")

#Set default value after invalid input/failed attempt
'''
If you don't to handle exception that occurred above, you can choose to put default keyword argument in the function.
This tells the function to return a default value if user failed to enter a valid input, hence preventing
exceptions from crashing the program.
'''
desireFood = pyip.inputMenu(["Cookie", "Bread", "Cake", "Ice Cream"],
                            prompt = "Please choose your food:\n", 
                            numbered = True, 
                            timeout = 5, default = "Cookie"
                            )
print(f"Alright! I will pass you the {desireFood} soon.")

#Regular Expression in pyinputplus
'''
You can use AllowRegexes & BlockRegexes keyword arguments to specify the pattern of accepted and rejected inputs.
Both keyword arguments takes a list of Regex which you can check for user input.
Note that if AllowRegexes & BlockRegexes contain conflicting Regex, then AllowRegexes will overwrite BlockRegexes.
'''
TwentyFourHourTimeFormat = r"\d{4} hrs"
time = pyip.inputNum("Please enter a time: ", allowRegexes = [TwentyFourHourTimeFormat])
print(f"The time you entered is {time}.")

HelloWordRegex = r"Hello World"
DestroyWorldRegex = r"World"
msg = pyip.inputStr("Say something: ", allowRegexes = [HelloWordRegex], blockRegexes = [DestroyWorldRegex])
print(msg)