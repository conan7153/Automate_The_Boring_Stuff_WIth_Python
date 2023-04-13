'''
Project requirements:
1, Walk through a directory tree, get the file size info of those exceptionally large files(> 100 MB)
2, List down the absolute path of these files, prompt users to see whether they want to delete them
3, User can decide which files to delete by typing the index number provided in the list
'''
#TODO Walk down directory tree, get absolute path of the large files, put them in a list called target list
import os, sys
from pathlib import Path
scanDirectory = input("Please enter the path of the directory that you want to do the file scan: ")
os.chdir(Path(scanDirectory))
largeFileList = []
minFileSize = int(input("Please enter the file size limit(GB) for file selection.\nAny files greater than this would be selected: "))
for currentfolder, subfolderList, fileList in os.walk("."):
    for filename in fileList:
        if os.path.getsize(Path(currentfolder)/filename) > minFileSize * (10 ** (3 * 3)):
            largeFileList.append(Path(currentfolder)/filename)

print("=" * 60)
if largeFileList:
    print(f"Larget files detected in {Path(scanDirectory)}:")
    for index, filepath in enumerate(largeFileList):
        print(f"{index + 1}, {filepath}")
else:
    print(f"No match file found in {Path(scanDirectory)}")
    sys.exit()
#TODO using while loop to get the list of index of files that the user wants to delete, then delete the files after user confirm

targetList = []
while True:
    
    userInput = input("""Plese choose your action:
        *Input index to choose file that you want to delete.
        *Input "delete" to delete the files that you have choosen.
        *Input "list" to view the list of files that you have choosen.
        *Input "deselect" to deselect the file that you have selected.
        *Input any other keys to quit the program: """)
 
    if userInput.isnumeric():
        if largeFileList[int(userInput) - 1] not in targetList:
            targetList.append(largeFileList[int(userInput) - 1])
            input(f"File{largeFileList[int(userInput) - 1]} selected.>")
        else:
            input("File aleady inside target list...>")

    elif userInput.lower() == "list":
        print("You are deleting the following files:")
        for index, filepath in enumerate(targetList):
            print(f"{index + 1}, {filepath}")
        input(">")

    elif userInput.lower() == "delete":
        print("You are deleting the following files:")
        for filepath in enumerate(targetList):
            print(f"{index + 1}, {filepath}")
        userInput = input("Are you sure you want to proceed? Enter 'Yes' to proceed, any other key to cancel.")
        if userInput == "Yes":
            for filepath in targetList:
                 os.unlink(filepath)
            input("The aboved files have been successfully deleted.")
            break
        else:
            continue
        
    elif userInput.lower() == "deselect":
        print("You are deleting the following files:")
        for index, filepath in enumerate(targetList):
            print(f"{index + 1}, {str(filepath)}")
        userInput = input("Please input the index of the file that you want to deselect.\nPress any other key to cancel: ")
        if userInput.isnumeric():
            input(f"File{targetList[int(userInput) - 1]} deselected from target list.")
            del targetList[int(userInput) - 1]
            
        else:
            continue

    else:
        sys.exit()
        
        

