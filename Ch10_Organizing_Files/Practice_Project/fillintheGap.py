'''
Project Requirement:
1, Scan through files in the directory with specific prefiex and suffix, save them in scanFileList
2, Scan through scanFileList, extract all the numbering in the filename
3, Spot the gap in the number store this in gapNumberList
4, adjust the filenames of the files behind the gap in order to fill up the gaps.
'''

import os
from pathlib import Path

workingDirectory = Path(r"C:\Users\Mao Weiqing\Documents\Python\Automate_Boring_Stuff\Ch10_Organizing_Files\Practice_Project\Spam")
os.chdir(workingDirectory)

scanFileList = []
for filename in os.listdir("."):
    filename = filename.strip("Spam")
    filename = filename.lstrip("0")
    filename = filename.rstrip(".txt")
    scanFileList.append(int(filename))

gapNumberList = []
for x in range(1, scanFileList[-1] + 1):
    if x in scanFileList:
        continue
    else:
        gapNumberList.append(x)

for number in gapNumberList:
    if len(str(number)) == 1:
        open(f"Spam00{number}.txt", "w")
    elif len(str(number)) == 2:
        open(f"Spam0{number}.txt", "w")
print("Gaps in filenames are filled.")

