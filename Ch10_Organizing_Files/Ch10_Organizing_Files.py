#Organizing Files
'''
You can modify the state of existing files such as copy, move, rename, delete them 
using python's built-in module shutil(shell utility)
'''
import shutil, os
from pathlib import Path

#copy() & copytree() methods
'''
copy(source, destination) copies a single file and paste it into new destination.
If the destination is a path, the file would be just pasted there with original name.
If the destination is a filename, the file would be renamed into that filename.
copytree(source destination) copies the folders and the files in the source and paste them into new destination.
Both functions return the new path of the copied file.

Note that for copy() if the filename for destination already exists, the content of that file would be overwritten.
For copytree(), if the filename or directory already exists, then FileExistsError will be raised.
'''
#shutil.copy(Path.cwd()/"1/Hello World.txt", Path.cwd()/"2/Hello World.txt")
#shutil.copy(Path.cwd()/"1/Hello World.txt", Path.cwd()/"3")

#Moving and renaming files
'''
You can use shutil.move(source destination) to move or rename a file.
If destination is a filepath, the file would simply be moved to the new directory.
If destination is a filename, the file would be moved and renamed at the same time.
If destination is a filename and the destination folder also have file with same name,
then the existing file would be overwritten by the moved file.
If destination folder does not exists, python would mistaken it as filename without extension.
If the directory pathway to the destination does not exist, then FileNotFound error would be raised.
'''
#shutil.move("./2/New World.txt", "./Test/")

#Permanently deleting files and folders
'''
You can delete single file or single empty folder with os module
If you want to delete one whole directory(including the folders and files),
then use shutil module
os.unlink(path)               Delete a single file
os.rmdir(path)                Delete an empty folder
shutil.rmtree(path)           Delete all subfolder and files in the directory
'''
#os.unlink("./Test/New World.txt")

#Safe deleting using send2trash module
'''
The above deleting method will permanently delete files and folders without anyway to undo the change.
Hence, if you want to safe delete(remove the file to computer's trash bin), use send2trash module's
send2trash() function.
Note that this module does not provide ways to restore file, hence if you want to restore file from trash bin
you have to manually do it.
'''
import send2trash
#send2trash.send2trash("./2/Hello World.txt")

#Walk through all folder and files in a directory
'''
If you want to scan through all the subfolders and files in the directory in order to access or modify the contents,
you can use os.walk() function and for loop to access them.
For each iteration of the for loop, os.walk() will return 3 values:
1, string value of the current folder for the iteration
2, list of string of subfolder name
3, list of string of file names inside this folder
Since 2 & 3 are list, you can access each of the element inside the list using for loop as well.
'''
for currentfolder, subfolder, filename in os.walk(".."):
    print(f"List of subfolders in {currentfolder}:")
    for folder in subfolder:
        print(folder)

    print(f"List of files in {currentfolder}:")
    for file in filename:
        print(file)
    print("")

#Working with zipfiles
'''
Python provides ways to interact with zipfiles, using the zipfile module
In order to work with a zipfile, you need to follow the steps below:
1, file = zipfile.ZipFile(filename) to get the ZipFile object.
2, Interact with the zip file using ZipFile object's various methods
3, Close the ZipFile Object using ZipFile.close() method. 
'''
import zipfile
example = zipfile.ZipFile("Spam.zip")

#Access info about the zip file
'''
ZipFile object provides many method that can access relevant info about this zip file
ZipFile.namelist() returns list of strings of folder names & filenames in the zip file
ZipFile.getinfo(filename) returns a ZipInfo Object which allows you to access info of specific file through 
different attributes.

ZipInfo.file_size means size of original file in integer(Byte)
ZipInfo.compress_size returns size of compressed file in integer(Byte)
'''
exampleInfo = example.getinfo("automate_online-materials/catnapping.py")
print("Original File Size: ", exampleInfo.file_size)
print("Compressed File Size: ", exampleInfo.compress_size)
print("Compression rate of this zip file is: {:.2f}".format(exampleInfo.compress_size/exampleInfo.file_size))
example.close()

#Extract content of zip file 
'''
You can extract the content of zip file using ZipFile object's extract() & extractall() methods.
extract(filename, destination) would extract the specified file to destination folder, it the destination folder
does not exists, then this folder would be created before extraction happens. 
If destination omitted, then file would be extracted to the current working directory.
The path of extracted file would be return by the function when extraction is successful.

extractall(destination) would extract everything inside the zip file, and behaves similarly as extract().
'''
#example.extract("automate_online-materials/catnapping.py")
#example.extractall("./ExtractTest/")

#Building & modifying your own zip files
'''
Just like the plain text file in the previous chapter, you can work with zip file in similar manner.
If you want to create a zip file, create a ZipFile Object in write mode.
1, newZipFile = zipfile.ZipFile("NewZipFile.zip", "w")
2, newZipFile.write(filename to be compressed, compression algorithm)

Note that same as previously, write mode will erase the original content in the zip file.
If you want to append files to existing zip file, then open ZipFile object in append mode.
'''
example = zipfile.ZipFile("Spam.zip", "a")
example.write("./1/Hello World.txt")
example.close()