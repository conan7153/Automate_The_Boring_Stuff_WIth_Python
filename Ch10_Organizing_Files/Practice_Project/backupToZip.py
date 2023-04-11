'''
Project requirements:
1,Backup the project folder(everything) into a zip file, include version number at the end of filename.
2, Everytime backup is done, update the version number of the zip file.
'''

import zipfile, os
from pathlib import Path


ProjectPattern = "Project*.zip"
destinationPath = "C:/Users/Mao Weiqing/Desktop/"

#Determine whether to create new file or update version
if list(Path(destinationPath).glob(ProjectPattern)) == []:
    ProjectZip = zipfile.ZipFile(Path(destinationPath)/"Project1.zip", "w")
else:
    for filename in list(Path(destinationPath).glob(ProjectPattern)):
      currentVersion = ""
      for char in str(filename.name):
            if char.isnumeric():
              currentVersion += char
    currentVersion = int(currentVersion) + 1
    ProjectZip = zipfile.ZipFile(Path(destinationPath)/f"Project{currentVersion}.zip", "w")
    os.unlink(Path(destinationPath)/f"Project{currentVersion - 1}.zip")

os.chdir("../../Ch9_Reading_and_Writing_Files")
for currentfolder, subfolderList, fileList in os.walk("."):
    ProjectZip.write(currentfolder)
    for file in fileList:
        ProjectZip.write(currentfolder + "/" + file)

ProjectZip.close()
