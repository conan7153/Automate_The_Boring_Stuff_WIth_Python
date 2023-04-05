#Single, Double Quote & Escape Signs
'''
Python allows defining of string using both ' and ". However, if you directly insert a quote in the string, 
python may take it as the end of a string. Hence you need to switch between ' and ", or use an escape sign
to tell python that the quote is actually part of the string.
'''
house1 = "Mr.A's Home."
presidentSpeech = 'The President says, "Making our country great again!".'
cat1 = 'Mr.A\'s cat.'

'''
Escape sign can be used to specify other special characters within a string, such as 
backslash, tab, newline etc.
'''
print("\tThis line starts with a tab.")
print("\\ is the escape sign.")
print("First line\nSecond line")

#Multiline strings & Multiline comment
'''
You can use multiline string which completely frees you from the need of escaping special characters.
You can use this method to write multiline comment in your program as well.
'''


msg = """
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
"""
print(msg)

#String slicing
'''
Since string are sequence data type, you can perform slicing on string just like list.
Note that slicing is extracting part of the data, not modifying the value itself.
'''
msg = "Hello World"
greeting = msg[0:5]
print(msg)
print(greeting)

#Checking string subset using in/not in operator
'''
Since string are sequence data type, you can use the in/not in operator to check
whether a string is a subset of another string.
'''
a = "Hello World"
b = "Hello"
print(b in a)
print(a in b)
print(a not in b)

#String Formatting
'''
Other than string concatenation & replication, you can perform string formatting which is called
string interpolation. This means you can put a string inside another string.
Currently python support 3 ways of doing this, which are % operator, .format() and f-string.
'''
userName = "Mr.A"
print("Good Moring %s" % (userName))
print("Good Afternoon {}".format(userName))
print(f"Good Evening {userName}")

#Useful String Methods
#upper(), lower() Methods
'''
upper(string) returns the string value passed with all upper case letters
lower(string) returns the string value passed with all lower case letters
Note that the original string passed is not modified.
'''
msg = "Hello World"
print(msg.upper(), msg.lower(), sep = "\n")

#isX() Methods
'''
Python offers a wide range of methods in the form of isX().
These methods basically checks whether a string fits certain conditions.
For example:
isupper() checks whether a non-empty string is all upper case.
islower() checks whether a non-empty string is all lower case.
isalpha() checks whether a non-empty string is all alphabetical.
isalnum() checks whether a non-empty string is all alpha-numerical(contains only letters & numbers)
isdecimal()/ isnumeric() checks whether a non-empty string is all numerical.
isspace() checks whether a non-empty string is all space, tabs and newlines.
istitle checks whether a non-empty string is all words that starts with capital letters
'''
print("Check string using isX() methods...")
print("hello".islower())
print("WORLD".isupper())
print("abcd".isalpha())
print("abc123".isalnum())
print("123".isdecimal())
print("456".isnumeric())
print("   \n".isspace())
print("This Is A Title.".istitle())

#startswith() & endswith() methods
'''
Checks whether a string starts/ends with certain strings.
'''
print("Check startswith & endswith")
print("Hello World".startswith("Hello"))
print("Hello World".endswith("World"))

#join() & split method
'''
string.join(list) joins the values in the list with string in between each value
string.split(string) split a string according the separator string specified,
if no string specified as separator, string will be splited according to space, tabs and newlines.
'''
print("and".join(["one", "two", "three", "four"]))
a = "Hello World"
print(a.split())
print(a.split("o"))

#Split string using partition() method
'''
partition(string) method will split the string into 3 parts: before, separator, after,
and return the result in the form of tuple - (before, separator, after)
if the separator is not found in the string, the 1st value in the tuple would be the string itself,
the 2nd and 3rd value in the tuple would be empty
You can make use of feature to split certain string into 3 parts, and quickly assign each value to
a variable using multi-assignmen trick in python.
'''
a = "5+7=12"
expression, equalSign, result = a.partition("=")
print(f"expression is {expression}.\nresult is {result}")

b = "Hello World"
print(b.partition("Goodbye"))

#Justify Text stored in string using ljust(), rjust() & center() methods
'''
ljust(len of justified string, filling character) justify text to the left.
rjust(len of justified string, filling character) justify text to the right.
center(len of justified string, filling character) justify text to the center.
2nd argument filling charcater is optional,space would be when not specified 
'''
print("Hello".ljust(20, "*"))
print("World".rjust(20, "="))
print("Goodbye World".center(20))

#Remove space or certain characters from the string using lstrip(), rstrip(), strip() methods
'''
lstrip(string) only strips off specified text from the string on its left side
rstrip(string) only strips off specified text from the string on its right side
strip(string) strips off specified text from the string from both sides
if no argument passed, space, tab & newlines would be striped off.
Note that the sequence of letter for the string argument does not matter
'''
print("    Hello World    ".lstrip())
print("       Goodbye World           ".rstrip())
print("******     New World****".strip("*"))
print("pSmaHello WorldmapSSpam".strip("Spam"))

#Convert Character and its unicode code point using chr() & ord() functions
'''
Since computer only understands 0 & 1, so computer scientists use combination of 0 & 1 to represent characters.
There are different conventions around the world for the computers to interpret different languages just by 0 & 1.
For example, ASCII(American Standard Code for Information Interchange) is used for english only computer.
However, ASCII is not suitable for languages like Chinese, Japanese and so on. Therefore, python adopts another
convention which is called Unicode.
Python provides functions to convert data between character & character unicode ordinal
ord(), returns the unicode ordinal of a character
chr(), returns the character that is tied to the unicode ordinal passed
'''
print(ord("A"))
print(chr(99))
