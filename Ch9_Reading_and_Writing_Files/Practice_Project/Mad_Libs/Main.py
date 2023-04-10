'''
Project requirements:
For the msg displayed below, replace all the keyword with an actual word and then write the result into
msg.txt 
'''

msg = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."

adjective = input("Please enter an adjective:\n")
noun = input("Please enter a noun:\n")
verb = input("Please enter a verb:\n")
noun2 = input("Please enter a noun:\n")

msg = msg.replace("ADJECTIVE", adjective, 1)
msg = msg.replace("NOUN", noun, 1)
msg = msg.replace("VERB", verb, 1)
msg = msg.replace("NOUN", noun2, 1)

with open("msg.txt", "w") as msgFile:
    msgFile.write(msg)
    print("Replaced text written to msg.txt file.")