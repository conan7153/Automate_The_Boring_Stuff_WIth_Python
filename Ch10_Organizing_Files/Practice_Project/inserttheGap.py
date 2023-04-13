'''
Project Requirement:
Same as the filling in the gap project, now you will be inserting a gap into such filenames
'''
import os, shutil
from pathlib import Path

workingDirectory = Path("C:/Users/Mao Weiqing/Documents/Python/Automate_Boring_Stuff/Ch10_Organizing_Files/Practice_Project/Spam/")
os.chdir(workingDirectory)

numberList = []
for filename in os.listdir("."):
    filename = filename.strip("Spam")
    filename = filename.rstrip(".txt")
    filename = filename.lstrip("0")
    
    numberList.append(int(filename))

insertIndex  = int(input("Please enter the index at which you want to insert the gap."))
targetList = []
for number in numberList:
    if number < insertIndex:
        continue
    else:
        targetList.append(number)
print(targetList)

for x in range(len(targetList) - 1, -1, -1):
    if len(str(targetList[x])) == 1 and len(str(targetList[x] + 1)) == 2: 
        shutil.move(f"Spam00{targetList[x]}.txt", f"Spam0{targetList[x] + 1}.txt")
    elif len(str(targetList[x])) == 2 and len(str(targetList[x] + 1)) == 2: 
        shutil.move(f"Spam0{targetList[x]}.txt", f"Spam0{targetList[x] + 1}.txt")
    else:
        shutil.move(f"Spam00{targetList[x]}.txt", f"Spam00{targetList[x] + 1}.txt")

print("Gap inserted and files reorganized.")

