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
Path.cwd() / filepath 
os.path.abspath(filepath)         convert a relative filepath to absolute filepath
os.path.relpath(filepath, start folder)         return the relative file path of a file relative to a starting folder
'''
filePath = "C:/Users/Mao Weiqing/Documents/Python/Automate_Boring_Stuff"
print(Path(filePath).is_absolute())
print(os.path.isabs(filePath))

fileName = "Ch9_Reading_and_Writing_Files.py"
absoluteFilePath1 = Path.cwd() / fileName
absoluteFilePath2 = os.path.abspath(fileName)
print(absoluteFilePath1, absoluteFilePath2, sep = "\n")

print(os.path.relpath("C:/Users/Mao Weiqing/Downloads", filePath))