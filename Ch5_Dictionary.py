#Dictionary
'''
Dictionary is a mutable data type that is different from List in many ways.
1, Dictionary is unordered, you can't access its values using index.
2, Dictionary contains key-value pairs, you can only access the values using the keys.
3, Unlike Index which can only be numbers, keys can be of any immutable data types, like int, float, string etc.
'''
dictionaryExample = {"key":"value", 1:"one", 2:"two", 3:"three", 4:"four"}

#Accessing Dictionary Values using Keys
'''
As mentioned aboved, you can access & modify values in dictionary in the form of dict[key].
Note that if you try to access a key that does not exist, KeyError error message would occur.
You can add new key value-pair into the dictionary by using similar syntax.
'''
a = {"key":"value", 1:"one", 2:"two", 3:"three", 4:"four"}
print(a["key"])

try:
    print(a["question"])
except KeyError:
    print("No such key in the dictionary")

a["question"] = "answer"
print(a)

#Dictionary are orderly-arranged since python3.7, but still not ordered
'''
When you convert a dictionary to a list using syntax like list(dict),
you will get a list of keys in the dictionary.
Since python3.7, the key-value pairs would be in the same order as 
it is when the dictionary is first created.
However, you should not rely on such feature because dictionary is unordered in nature,
and when you use python version 3.6 and below, this may introduce unexpected error in your code.
'''
print(list(a))

#Common dictionary built-in functions, keys(), values(), items()
'''
keys() returns sequence data type [dict_keys], that contains the collection of keys in the dictionary.
values returns sequence data type [dict_values], that contains the collection of values in the dictionary.
items() returns sequence data type [dict_items], that contains the collection of key-value pairs in the dictionary.
Since the return value is sequence data type, you can iterate through them using for loops, or check whether
a value is inside the dictionary using in/not in operaotr.
You can use list() to convert those sequence data types into lists if you need to modify the values. 
'''
print("Dictionary's built in return data types")
print(a.keys(), a.values(), a.items(), sep = "\n")
print("\nResult when you convert them into list")
print(list(a.keys()), list(a.values()), list(a.items()), sep = "\n")

if 1 in a.keys():
    print("1 is a key inside dictionary a")
if 6 not in a.values():
    print("6 is not a value inside dictionary a")

#dict.get() Method
'''
Checking keys in dictionary using dict.keys() can be tedious and troublesome.
You can use dict.get(key, makeup_value) method to do the following:
If key exists, get the value in the dictionary that is tied to this key.
If key does not exist, return the makeup_value instead.
''' 
a = {"key":"value", 1:"one", 2:"two", 3:"three", 4:"four"}
x = a.get("key")
y = a.get("hello", "world")
print(x, y, sep = "\n")

#dict.setdefault()
'''
If you want to check whether a key is inside a dictionary and add this key-value pair into
the dictionary if the key does not exist, then you can use dict.setdefault(key, default_value) method
Note that if the key exist in the dictionary, dict.setdefault() would not do anything.
'''
a = {"key":"value", 1:"one", 2:"two", 3:"three", 4:"four"}
a.setdefault(5, "five")
print(a)
a.setdefault(1, "Hello World")
print(a)

#Nested Dictionary
'''
You can nest dictionary into other dictionaries, however, since the keys of a dictionary can only be of 
immutable data types, and dictionary & List are mutable data, hence you can't put dictionary or List as
the key of another dictionary.
You can make use of nest dictionary to structure different kinds of data, as long as they are easy to
interpret.
'''
chessBroad = {"A1":"wPawn", "B3":"bKnight", "H5":"wQueen", "D7":"bBishop"}
ticTacToeBoard = {"TopLeft": "X", "Top": "O", "TopRight":"X",
                  "Left":"O", "Middle":"X", "Right": "X",
                  "BottomLeft": "X", "Bottom": "O", "BottomRight":"O"}
packingList = {"Mr.A": {"ToothBrush": 2, "ToothPaste":1, "Mug":2},
               "Mrs.A": {"Picnic Mat": 1, "Lunch Bento Set": 2, "Utensils": 2},
               "Mr.B": {"Charcoal": 5, "Picnic Table": 1, "BBQ Equipment": 1}}