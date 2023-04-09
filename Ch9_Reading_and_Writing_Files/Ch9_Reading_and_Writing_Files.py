#Read & Writing Files
'''
Variables are good ways of storing different kinds of data, but if you want to store persistent data
about a system, then you will have to store these data explicitly in the computer as files.
Computer recognize a file by its path and filename, such as 'C:/User/Python/Ch9_Reading_and_Writing_Files.py'
Note that Windows, MacOs & Linux present file paths in different formats, hence if you want your python file
to be able to run on different OS, then you will have to use pathlib module to achieve this.

pathlib.Path() method combines the series of strings you put as argument, and return the result a valid filepath
for the current OS as [OS]Path objects.
To get the path string, pass the path object to str() function.
'''
from pathlib import Path
import os
filePath = Path("C:", "Users", "Python", "Ch9_Reading_and_Writing_Files.py")
print(type(filePath),filePath, sep = "\n")

#Difference between file path in Windows, MacOS & Linux OS
'''
Windows OS uses \ as separator for directories, while MacOS & Linux use / instead.
As a result of this, \ is not allowed to be part of filename in Window while it is 
allowed in MacOS & Linux.
Also, if you writing windows file path as string, write it either as raw string or
use escape sign to represent \ as separator.
'''
windowFilePath1 = "C:\\Users\\Python\Ch9_Reading_and_Writing_Files.py"
windowFilePath2 = r"C:\Users\Python\Ch9_Reading_and_Writing_Files.py"
print(windowFilePath1, windowFilePath2, sep = "\n")

#Appending Existing File Path in Path Object using / operator
'''
You can use string concatenation to join filename and path together, however, as mentioned above this is not
the best solution due to difference in filepath format for different OS.
Path Object does not only provide you with valid filepath for different OS, but also allows to modify filepath
that can instantly work on any OS.
Note that if you are using multiple / to join Path Object and string, at least 1 of the first 2 data in the expression
must be Path Object, because / does not support joining of 2 strings.
'''
RootFolderPath = Path("C:\\")
DocumentPath = Path("Users", "Document")
print(RootFolderPath / DocumentPath)

EDriveDocumentPath = "D:\\" / DocumentPath
print(EDriveDocumentPath)

#Current Working Directory
'''
If a filename does not include the root folder(C:/), then computer will interpret the whole filename as 
current working directory + filename.
You can use Path.cwd()/os.getcwd(for older python version) to get the current working directory.
os.chdir() can be used to change the current working directory.
If you try to change to a path that does not exist, FileNotFoundError will occur.
PS: Path Object current does not have similar function as os.chdir(), because anyhow changing cwd may
introduce bug into the system and cause the program to crash.
'''
print(Path.cwd())
os.chdir(r"C:\Users\Mao Weiqing\Desktop")
print(os.getcwd())

try:
    os.chdir("C:/This_Filepath_Does_Not_Exist")
except FileNotFoundError:
    print("File that you are looking for does not exist.")

os.chdir(r"C:\Users\Mao Weiqing\Documents\Python\Automate_Boring_Stuff")
print(Path.cwd())

#Home directories
"""
Each OS has a home directory which stores the files and data of each user on the system.
For Windows, it is C:\\Users
For MacOS, it is \/Users
For Linux, it is \/home (Escaping put here because of python's stupid feature)
Home directory is one of the directory in the computer that would certainly grants you permission
to modify the files within it, hence good for practicing working with files.
You can access home directory using Path.home() function.
"""
print(Path.home())

#Absolute Path VS Relative Path
'''
There are two ways of representing a file path: absoulte & relative filepath.
Absolute filepath always begin with the root directory, for example: C:\\
Relative filepath means the file's relative pathway from the current working direcotry.
In filepath, you can use special notations to represent the relative filepath.

. means the current/this folder
.. means the parent folder of this folder

For example, for C:\\Users\\Desktop & C:\\Users\Document, take cwd as Desktop:
Relative filepath for Document is ..\\Document
Relative filepath for C:\\ is ..\\..\. or ..\\..
'''

#Create New Directories
'''
Both os and pathlib modules provide function to create file directories.
Path(filepath).mkdir() creates a new directory once at a time
os.makedirs(filepath) creates multiple directory at one time to ensure the filepath entered is valid.
'''
#os.makedirs("C:/Users/Mao Weiqing/Documents/Python/Automate_Boring_Stuff/HelloWorld/GoodbyeWorld/DestroyWorld")
#Path("C:/Users/Mao Weiqing/Documents/Python/Automate_Boring_Stuff/Anything").mkdir()

#Handle Assolute & Relative Path
'''
There may be situations when we need to know the absolute filepath of a file, or the relative filepath from
one folder to another, there are some ways to convert filepath between absolute & relative ones

Path(filepath).is_absolute() 
os.path.isabs()                   checks whether the filepath is an absolute filepath

Path(filepath).absoulte()
os.path.abspath(filepath)         convert a relative filepath to absolute filepath

Path(filepath).relative_to(start folder)
os.path.relpath(filepath, start folder)  return the relative file path of a file relative to a starting folder
'''
filePath = "C:/Users/Mao Weiqing/Documents/Python/Automate_Boring_Stuff"
print(Path(filePath).is_absolute())
print(os.path.isabs(filePath))

fileName = "Ch9_Reading_and_Writing_Files.py"
absoluteFilePath1 = Path.cwd() / fileName
absoluteFilePath2 = os.path.abspath(fileName)
print(absoluteFilePath1, absoluteFilePath2, sep = "\n")

print(os.path.relpath("C:/Users/Mao Weiqing/Downloads", filePath))

#Getting part of a file path
'''
Both pathlib and os modules provides ways to split a file path into different parts, which allows us to work on
different file paths more easily.

For Path object, there are various attribute that you can call to get different parts of the file path:
anchor - The root folder of the file path, including the slash(only for window)
drive - The letter that specify the drives of the root folder, such as C for C Drive
parent - The hierachy of folders that includes the file
parents - Evaluates to ancestor folders with integer index(Path(filepath).parents[0] etc.)
name - filename
stem and suffix - stem refers to filename, suffix refers to file extension
Calling these attributes would return string of the relevant parts, except for parent which returns another Path
Object

For os modules, filepath are divided into 2 parts:
dirname - directory name which contains the file
basepath - filename
To get individual part, use os.path.split() to get a tuple containing both values.
To get list instead of tuple, use string method split() and os.sep(which represents the correct slash to use
which dividing file directory for the current OS) to get list of strings of individual parts.
'''
print("For Path object showcase:")
filepath1 = Path.cwd() / "Ch9_Reading_and_Writing_Files.py"
print(f"""For filepath {filepath1}:
anchor is {filepath1.anchor}, showing that the root folder is in {filepath1.drive} Drive
parent is {filepath1.parent}
full filename is {filepath1.name}
which contains {filepath1.stem} as stem & {filepath1.suffix} as file extension
the folder above this file is {filepath1.parents[0]}
follow by {filepath1.parents[1]}...
{filepath1.parents[2]} etc.""")

print("For os.path showcase:")
filepath2 = Path.cwd() / "RandomFile.py"
print(f"""For filepath2 {filepath2},
the dirname is {os.path.dirname(filepath2)}
the basename is {os.path.basename(filepath2)}
using os.path.split(filepath2) you will get {os.path.split(filepath2)}
using str(filepath).split(os.sep) you will get {str(filepath2).split(os.sep)}
""")

#Getting file size & list down all the sub folder and files
'''
Path(filepath).stat().st_size 
os.path.getsize()                Return integer to show file size in bytes

list(os.glob("*"))
os.listdir(filepath)             Return list of sub folders and files
'''

print("File size of this file is: ", (Path.cwd() / "Ch9_Reading_and_Writing_Files.py").stat().st_size)
totalFileSize = 0
for file in os.listdir():
    totalFileSize += os.path.getsize(file)
print("Total file size in this folder is: ", totalFileSize)

#Modify specific files with Path.glob() method
'''
Just like regular expression, command line also provides simple notation for expression filenames:
* refers to multiples of any characters, . refers to any single characters
For example, ".txt" refers to any filenames in .txt format etc, such expression is called glob pattern.
By passing glob pattern to glob() method, you will get a generator of matching files, you can then pass
this generator to list() method to view the content.
'''
print(list(Path.cwd().glob("Ch*.py")))
print(list(Path("C:/Users/Mao Weiqing/Desktop").glob("*")))

#Checking whether a filepath is valid, and whether is represents a file or directory
'''
Python will crash if you are referring to an invalid filepath, hence it is important to check the path's validity
before working on it. You can also apply methods to check whether it is a directory or file.
Path(filepath).exists()
os.path.exists(filepath)                 return Boolean value to check whether the filepath is valid or not

Path(filepath).is_file()/is_dir()        
os.path.isfile(filepath)/isdir(filepath) return Boolean value to check whether it is a file or directory
'''
print(Path.cwd().exists())
print(os.path.exists("This/diectory/does/not/exists"))

print(Path.cwd().is_dir())
print(os.path.isfile(Path.cwd() / "Ch9_Reading_and_Writing_Files.py"))

#Work with files by reading and writing them
'''
There are two types of files in the computer system - plaintext files & binary files
Plaintext files only contains text and no other info such as font, color, size etc. (txt files, py files)
Binary files contains more info than that (word docx, excel spreadsheet, images, PDF, exe files)

For python, the most common way of working on plaintext files in using open() function & file object.
1, open(filename) to open the file as file object.
PS:If you open file as write mode and this file does not exist, then python will create this file automatically.
2, read or write on the file using file object's read()/write() methods.
PS:File object is read mode by default, if you want to write files you need to open files in write mode, 
like open(filename, "w").
When file is written by python code, the original content would be erased, if you want to add text to existing
content then use "a" to open file in append mode.
If you want to interact with the files in multiple ways at the same time, simply use "r+", "w+", "a+"
3, after work done, close the file object using close() method.
'''
textFile = open("Appendix.txt", "w")
print(textFile.write("Hello World.\nThis my first time working on files using python."))
textFile.close()

with open("Appendix.txt", "r") as textFile:
    print(textFile.read())

"""
You can read the content of the file line by line using file object's readlines() method instead, this returns list
of strings which represents each line of text in the file.
Note that if you use readline() method instead, only string value of one line would be returned.
"""
with open("Appendix.txt", "r") as textFile:
    print(textFile.readlines())

"""
Each file has a pointer which points the current location of text that it has read. Hence if you need to read
the whole content of a file multiples when it is opened, you need to reset the pointer back to the start of the
whole text using seek(0) method
"""
file = open("Appendix.txt")
print(file.read())
print(file.read())
file.seek(2)
print(file.read())

'''
There's another way of reading and writing file, which is done by using pathlib module.
Path(filepath).read_text() 
Path(filepath).write_text()
However, the default way that python provides is more recommended.
'''
print((Path.cwd()/"Appendix.txt").write_text("This piece of text is written to the file using pathlib module."))
print((Path.cwd()/"Appendix.txt").read_text())

#Storing Persistent Data using shelve module
'''
In order to save data(game save, account balance etc.) we need to store those data outside python program,
we need to save them as persistent data, this can be done in python using the shelve module.
shelve module provides shelve value which acts in similar ways as dictionary, and store data in key-value pairs.
1, use shelve.open(shelf name) to get a shelf value and assign it to a variable
2, use variable[key] = value to store your data to the shelf value
3, use variable.close() to close the shelf
'''
a = [1,3,5,7,9,123]
import shelve
listShelf = shelve.open("listdata")
listShelf["a"] = a
listShelf.close()

listShelf = shelve.open("listdata")
b = listShelf["a"]
print(b)