#Finding string of certain format using basic python skills
'''
Just like webpage/Microsoft Words Ctrl+F Search feature, we can implement text search in python as well.
Below shows a basic way of searching american phone numbers using only python basic skills.
'''
def isPhoneNum(text):
    if text[0:3].isnumeric() and text[3] == "-" and text[4:7].isnumeric() and text[7] == "-" and text[8:12].isnumeric():
        return True
    else:
        return False

def extractPhoneNum(msg):
    for i in range(len(msg) - 12):
        text = msg[i:i+12]
        if isPhoneNum(text):
            print(f"New Phone Number Extracted: {text}") 

msg = "my office number is 123-456-7896.If you want to find me out of office hour, call me personal number 987-654-3210."
extractPhoneNum(msg)
        
#Regular Expression
'''
However, even though the above method works, it is not the most efficient way of solving such problem.
If the phone number we search has different possible format, then adding even more conditions to enable such search
would be tedious and hard to troubleshoot. 
Therefore, we should use regular expression to approach this problem instead.
Basic grammar for Regular Expression:
\d for digital characters, \w for any word character(letters, numbers, underscore), \s for space, tab and newlines
\D, \W, \S are the opposite of above.
{} is a short form of writing repetitive patterns: \d{3} means 3 consecutive digital characters.
'''
americanPhoneNumRegex = r"\d{3}-\d{3}-\d{4}"

#Using Regular Expression to search string
'''
To use Regex to search text in a string, you need to import re module to access relevant functions.
re.compile(Regex) returns Regex Object(RO)
RO.search(string to be searched) return Match Object(MO)
MO.group() returns the matched text from the string you provided

You can use RO.findall(string to be searched) to get a list of all matching text.
'''
msg = "my office number is 123-456-7896.If you want to find me out of office hour, call me personal number 987-654-3210."
import re
RO = re.compile(americanPhoneNumRegex)
MO = RO.search(msg)
print(MO.group())

print(RO.findall(msg))

'''
Above are examples in the book, I realise that re module iteself has 
search(Regex, string to be searched) 
match(Regex, string to be searched) 
findall(Regex, string to be searched) 
functions,
which runs similarly as above. 
'''
print(re.search(americanPhoneNumRegex, msg).group())
print(re.findall(americanPhoneNumRegex, msg))

#Grouping in Regular Expression using ()
'''
You can separate a Regular Expression into meaningful parts, and access only parts of the matched text
using the Matched Object's group() & groups() methods.
Take Regex r"(Area Code)(Phone Number)" as example. (Area Code) is group 1, (Phone Number) is group 2.
MO.group(1) will return matched string Area Code only, MO.group(2) returns matched string Phone Number only.
MO.group() returns the whole matched string as one single string.
MO.groups() returns tuple of groups, which allows you to apply multi-assignment trick.
'''
sgPhoneNumRegex = r"(\+65)(\d{8})"
RO = re.compile(sgPhoneNumRegex)
msg = "+6512345678"
MO = RO.search(msg)

x = MO.group(1)
y = MO.group(2)
print(x,y,sep = "\n")

print("Difference between group() & groups()")
print(MO.group())
print(MO.groups())

#Escaping Special Characters in Regular Expression
'''
As shown above, \ is placed in front of + because + is a special character that is meaningful in
Regular Expression. If you just want the regular expression to match this specific character, then
you need to escape the character using \, which is the same as escape sign for string.
Some special characters in Regex includes:
\()[]{}|?*+^$.
'''


    