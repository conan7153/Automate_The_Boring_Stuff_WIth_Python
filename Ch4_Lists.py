#List
'''
List is a value that stores other values in it in an orderly manner.
The values stored inside List are called item.
You can access the items in a List using index.
'''
a = [1,2,3,4]
b =["one", "two", "three", "four"]

print(a[3])
print(b[2])

#Index
'''
For most programming languages as well as python, the index of a list starts from 0.
Therefore for the last value in the list, its index is the length of the list - 1.
'''
a[0] == 1
a[1] == 2
a[2] == 3
a[3] == 4

b[0] == "one"
b[1] == "two"
b[2] == "three"
b[3] == "four"

'''
Similarly, you can access list items in reverse orders by using negative index.
'''
a[-1] = 4
a[-2] = 3
a[-3] = 2
a[-4] = 1

b[-1] = "four"
b[-2] = "three"
b[-3] = "two"
b[-4] = "one"

'''
You can change or delete the value stored in the list by using index.
Or delete the item using del keyword
'''
a[0] = 5
b[0] = "five"
del a[3]
del b[3]
print(a,b,sep = "\n")

#List Slicing using Index
'''
You can extract part or all part of a List using List Slicing
List Slicing format: [a:b:c]  
a for starting index, b for ending index(excluding value at ending index), c for stepping
if a omitted, sliced list assumed to be starting from the start of the list
if b omitted, sliced list assumed to be ending at the end of the list
if c omitted, the stepping taken when slicing the list assumed to be 1.
c can be negative, means stepping takes place in reverse order.
'''
a = [1,2,3,4,5]
a[0:5:1]      #[1,2,3,4,5]
a[2:4]        #[3,4]
a[2:5]        #[3,5]
a[:3]         #[1,2,3]
a[3:]         #[4,5]
a[::-1]       #[5,4,3,2,1]

#Accessing Length of a List using len() Function
a = [1,2,3,4,5]
print(len(a))

#List Concatenation & Replication
'''
You can perform list concatenation & replication, just like string.
'''
a = ["Hello"]
b = ["World"]
c = a + b    #["Hello", "World"]
d = a * 3    #["Hello", "Hello", "Hello"]

#Putting list inside list & Access the values using multiple indexes
multiList = [[1,2,3],[4,5,6],[7,[8,9]]]
multiList[0]       #[1,2,3]
multiList[1][2]    #6
multiList[2][1]     #[7,[8,9]]
multiList[2][1][0]   #8

#Multiple assignment tricks
'''
You can assign the values in a List to different variables at the same time.
This method is called List Unpacking. 
Do note that the number of variables and the number of values in the List must be the same.
'''
a = [1,2,3]
x, y, z = a      #x = 1, y = 2, z = 3

#Using for loops to access elements in a List
a = [1,2,3,4,5]
for number in a:
    print(number)

#In & not in Operators
'''
You can check whether a value is in or not in a List by using the in or not in operators.
'''
print(5 in a)
print(6 not in a)

#enumerate function
'''
You can access both the index & the value of a List by using the enumerate function
'''
a = [1,2,3,4,5]
for index, value in enumerate(a):
    print(f"a[{index}] is {value}.")

#Methods
'''
Methods are built in functions for object/classes
Since python treats a lot of its features as object, you can call methods that are associated
with these object/classes
List belongs to list class, hence you can call list function to perform certain actions on List
For example

index(value)                finding index of a value inside the list where it appears for the first time
append(value)               append a value to the end of the list
insert(index, value)        insert a value at a specified index in the list
remove(value)               remove the first instance of a value from the list
sort(reverse = True/False)  sort the numerical list in ascending order, or reverse sorting in descending order
sort(key = str.lower)       sort the alphabetical list in alphabetical order, pass key = str.lower to ignore case sensitivity
reverse()                   reverse sequence in the list
'''

#Line continuation Operator \
'''
You can insert \ operator inside a python code to tell computer that the line continues on the next line.
This is useful(?) if you want to structure your python code in a nicer format.
'''



