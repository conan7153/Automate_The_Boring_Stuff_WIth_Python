'''
Project Requirement:
1, walk through a directory tree, identify all files with specific extension(.jpg,.pdf,.png etc.)
2, copy all these files into a new folder
3, zip up the file for backup
'''
import os, shutil, zipfile
from pathlib import Path

#TODO use os.walk() to walk through targeted directory
targetPath = Path("C:/Users/Mao Weiqing/Documents/Others/Memory Forest/Memory_Forest_The_Pandora_Box/Memory_Forest_The_Pandora_Box/")
destinationPath = Path("C:/Users/Mao Weiqing/Desktop/Copied_Folder/")

os.chdir(targetPath)
targetList = []
for currentfolder, subfolderList, fileList in os.walk("."):
    for filename in fileList:
        if str(filename).endswith(".png"):
            targetList.append(Path(currentfolder)/filename)

if os.path.exists(destinationPath):          
    for file in targetList:
        shutil.copy(file, destinationPath)
else:
    destinationPath.mkdir()
    for file in targetList:
        shutil.copy(file, destinationPath)

#TODO zip up this folder into zipfile using zipfile.Zipfile() method
os.chdir(destinationPath)
imageZip = zipfile.ZipFile(Path("../ImageZip.zip"), "w")
for file in os.listdir("."):
    imageZip.write(file)
imageZip.close()