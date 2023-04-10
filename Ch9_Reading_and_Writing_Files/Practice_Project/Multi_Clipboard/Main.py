'''
Project requirements:
1, Users can have the message that correspond to the keyword they entered in the prompt copied to clipboard.
2, Users can update the table of keywords externally in the prompt by entering Main.py save [keyword]
to have the current message in the clipboard saved in the table in the form of {keyword:message}
3, Users can access the list of available keywords in the system by typing Main.py list, the list of keywords
would be in alphabetical orders.
'''
import pyperclip as pyclip
import sys, shelve

#Open Shelve to save persistent data
keywordShelf = shelve.open("mcbkeyword")

#Save and update shelve value 
if len(sys.argv) == 3:
    filename, save, keyword = sys.argv
    keywordShelf[keyword] = pyclip.paste()
    print(f"Message for {keyword} successfully saved.")

#Copy value from shelve and paste to clipboard
elif len(sys.argv) == 2:
    filename, keyword = sys.argv
    if keyword.lower() in keywordShelf.keys():
        pyclip.copy(keywordShelf[keyword])
        print(f"Message for {keyword} successfully copied to clipboard.")

    #List down all existing values in shelve
    elif keyword.lower() == "list":
        keywordList = list(keywordShelf.keys())
        keywordList.sort(key = str.lower)
        for key in keywordList:
            print(key)

    #Keyword not found error message
    else:
        print(f"No Message found for keyword {keyword}\nYou can use Main.py save [keyword] to save message into the system.")

#Close the shelve when the program terminates
keywordShelf.close()

#This file supposed to function like a module, do not open it as a main file
if __name__ == "__main__":
    pass