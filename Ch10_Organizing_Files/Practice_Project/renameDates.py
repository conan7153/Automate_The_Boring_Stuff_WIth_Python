import shutil, re, os

#Access all the files in the folder
#Use regex to scan all filenames with american date
#Rename files using shutil.move() function

americanDateFilenameRegex = r"(\d{2})(\d{2})(\d{2})"

for file in os.listdir("./AmericanDateFiles/"):
    if re.search(americanDateFilenameRegex, file) != None:
        modifedFilename = re.sub(americanDateFilenameRegex, r"\2\1\3", file)
        shutil.move(f"./AmericanDateFiles/{file}", f"./AmericanDateFiles/{modifedFilename}")

print("Dates in the files have been changed into DD/MM/YY format.")