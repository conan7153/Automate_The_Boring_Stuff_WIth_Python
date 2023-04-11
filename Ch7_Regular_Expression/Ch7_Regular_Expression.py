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

#Search either X or Y string using |(Pipe) Operator
'''
| Operator will return a matched text if either Regex has a matched pattern in the string you want to search.
The first occurrence of such matched text will be returned.
Note that you use RO.findall() method, then all the matched text will be returned.
'''
XorYRegex = r"X|Y"
RO = re.compile(XorYRegex)
msg = "This sentence has both Y and X."
MO = RO.search(msg)
print(MO.group())
print(RO.findall(msg))

'''
You can combine | and () to match different alternative patterns which are similar in some ways.
'''
HeroRegex = r"(Spider|Bat|Super)man"
msg = "Batman fights the war together with Spiderman and Superman."
RO = re.compile(HeroRegex)
MO = RO.search(msg)
print(MO.group())
print(RO.findall(msg))

#Optional matching with ? operator
'''
In regular expression, you can use ? operator to specify a group which is optional to match.
Regular Expression will match the string, if this optional part does not occur or occur only once
in the string.
'''
PoliceRegex = r"police(wo)?man"
msg = "My mother is a policewoman, my sister is going to become a policewoman."
RO = re.compile(PoliceRegex)
MO = RO.search(msg)
print(MO.group())

SGPhoneNumRegex = r"(\+65)?(\d{8})"
msg = "My phone Number is 12345678, Singapore office phone number, call +6587654321"
RO = re.compile(SGPhoneNumRegex)
print(RO.findall(msg))

#Matching no or unlimited repetition of a pattern using * operator
'''
* provides similar feature as ?, except for the fact that it can match pattern that
either does not appear or pattern that repeats over countless number of times.
'''
HelloWorldRegex = r"(Hello)* World"
msg1 = "Hello World"
msg2 = " World"
msg3 = "HelloHelloHello World"
print(re.search(HelloWorldRegex,msg1).group())
print(re.search(HelloWorldRegex,msg2).group())
print(re.search(HelloWorldRegex,msg3).group())

#Matching at least one occurrence of a pattern using + operator
'''
+ operator will match string that occurs at least once, at least the matching pattern occurs,
it does not matter how many times that pattern occurs.
'''
HelloWorldRegex = r"(Hello)+ World"
print(re.search(HelloWorldRegex,msg1))
print(re.search(HelloWorldRegex,msg2))
print(re.search(HelloWorldRegex,msg3))

#Specify a range of repetition that you can accept using {min, max} syntax
'''
\d{x} means matching text with x number of digital characters.
You can specify a max & min boundary for text matching.
As long as the number of repetition of pattern lies within the range specified, 
regular expression will take this text as matched text. 
if min, max is omitted, then the lower/upper limit is considered as 0/infinite
'''
HaHaHaRegex = r"(Ha){3,5}"
msg = "Ha HaHa HaHaHaHa"
print(re.search(HaHaHaRegex, msg).group())

#Greedy & Non-greedy search
'''
For ambiguous situation, Regex will match the longest string that fits itself, this is Greedy Search.
On the other hand, you can specify Non-greedy(lazy) search by using {min, max}? syntax instead.
In this case, Regex will match the shortest string that fits itself instead.
'''
ambiguousMessage = "HaHaHaHaHaHa"
greedySearch = r"(Ha){3,5}"
lazySearch = r"(Ha){3,5}?"
print(re.search(greedySearch, ambiguousMessage).group())
print(re.search(lazySearch, ambiguousMessage).group())

#findall() method
'''
While search() method returns you only the first instance of matched text,
you can get a list of all matched strings by using findall() method.
If Regex passed into the method does not have groups, findall() returns a list of matched strings.
If Regex passed into the method has groups, findall() returns a list of tuples of strings,
each item in a tuple corresponds to the groups in the Regex.
'''
SGPhoneNumRegex1 = r"\+65\d{8}"
SGPhoneNumRegex2 = r"(\+65)(\d{8})"
msg = "My phone number is +6512345678, you may try +6587654321 as alternative."
print(re.findall(SGPhoneNumRegex1, msg))
print(re.findall(SGPhoneNumRegex2, msg))

#Making your own character class using []
'''
As mentioned previously, \d,\s,\w,\D,\S,\W represents different types of characters.
Such notation is called character class, and you can specify your own character class
using [].
For example, [aeiouAEIOU] represents all characters that are vowels.
You can use hyphen - to specify range of characters: 
[A - Z] represents all capital letters. 
[A-Za-z] represents all letters only.
You can put a ^ sign right after [ to specify a negative character class, the Regex will
match all characters that are not inside the negative character class:
[^0-9] represents non-numeric characters
[^A-Za-z]represents non-alphabetical characters
[^AEIOUaeiou] represents consonants.
'''
VowelRegex = r"[AEIOUaeiou]"
ConsonantRegex = r"[^AEIOUaeiou]"
msg = "svanonfaefawignoewfanfoingowiefaw"
print(re.findall(VowelRegex, msg))
print(re.findall(ConsonantRegex, msg))

#Matching Start & End of string using ^ and $ operator
'''
If you need to match a string whose start or end follows a certain pattern, then we can use ^ and $ operator
to specify the starting and ending pattern of the matched text.
If ^ and $ are used together, this means the matched text must exactly follow the Regex pattern.
'''
StartswithHelloRegex = r"^Hello"
EndswithHelloRegex = r"Hello$"
msg1 = "Hello World"
msg2 = "Hey Hello"
print(re.search(StartswithHelloRegex, msg1))
print(re.search(StartswithHelloRegex, msg2))
print(re.search(EndswithHelloRegex, msg1))
print(re.search(EndswithHelloRegex, msg2))

NumberFilterRegex = r"^\d+$"
msg1 = "12334252592890258903"
msg2 = "1241231asdfjafoawje1142413241"
print(re.search(NumberFilterRegex, msg1))
print(re.search(NumberFilterRegex, msg2))

#Match any character other than new line using . operator
'''
If you want to match literally anything that is in a string except for newline characters, then 
you can use . operator represent such pattern.
. just match one character only, if you want get everything then use * or + according to your need.
Such match is greedy by default, if you want non-greedy search then put a ? operator behind, like .*?
'''
GreedyRegex = r"\(.*\)"
LazyRegex = r"\(.*?\)"
msg = "((Hello World), this is my first python program.)"
print(re.search(GreedyRegex, msg).group())
print(re.search(LazyRegex, msg).group())

#List of all Regex operators 
'''
| for multiple Regex
? for optional pattern in Regex
* for 0 to unlimited occurrence pattern
+ for at least one occurrence pattern
() for grouping in Regex
{x} for specifying number of occurrence pattern
{x, y} for greedy search
{x, y}? for non-greedy search
[] for specifying custom character class
[^] for specifying negative class
^ for specifying pattern at the start of string
$ for specifying pattern at the end of string
. for matching any character other than newlines
\ for escaping special characters
'''

#flag argument in regular expression method
'''
You can pass flag argument to re modules function to enable certain searching or formatting feature.
For re.compile(), you can pass this as the 2nd argument. 
If you are using re.search(), re.match(), re.findall() instead, this would be the 3rd argument.
re.IGNORECASE/re.I enables case-insensitive search in regular expressions.
re.DOTALL enables . operator to match newline character as well.
re.VERBOSE allows you to format your Regex in nicer format for greater readability.
If you want to pass more than 1 flag argument to re function, write it as
re.compile(Regex, re.I|re.DOTALL|re.VERBOSE)
'''
HelloWorldRegex = re.compile(r"Hello World", re.I)
DotAllRegex = re.compile(r".*", re.DOTALL)
msg = "HELLO WORLD\nGOODBYE WORLD"
print(HelloWorldRegex.search(msg).group())
print(DotAllRegex.search(msg).group())

phoneNumRegex = re.compile(r"""（
(\d{3}|\(\d{3}\))?     #Area Code
(\s|-|\.)?             #separator
\d{3}                  #first 3 digits
(\s|-|\.)              #separator
\d{4}                  #last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5}?
)""", re.VERBOSE)

#Substituting matched text with other values using sub() method
'''
RO.sub(string to replace, string to be replaced)
Returns the substituted string
Note that all matched text would be replaced at the same time.
'''
helloRegex = re.compile(r"hello", re.I)
msg = "hellohello"
msg = helloRegex.sub("goodbye", msg)
print(msg)

'''
For replacement string of sub() method, notation \1, \2, \3 etc. means the corresponding group
in the matching Regex. 
'''
dateFilename = "RandomFile100423.txt"
dateRegex = ".*(\d{2})(\d{2})(\d{2}).*"
print(re.sub(dateRegex, r"\3\2\1", dateFilename))
