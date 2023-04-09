'''
Project Requirement:
Generate 35 randomized copies of exam papers(in .txt files) to prevent students from cheating.
The options and the question sequence are to be randomized.
'''

import random, os
from pathlib import Path

#Generate Test Question Dictionary
TestQuestionDictionary = {}
with open("Test_Paper.txt", "r") as paper:
    for quiz in paper.read().split("\n\n"):
        question, option1, option2, option3, option4 = quiz.split("\n")
        TestQuestionDictionary[question] = [option1, option2, option3, option4]

#Generate Answer Table
TestAnswerDictionary = {}
with open("Test_Answer.txt", "r") as answer:
    for question in answer.readlines():
        key, ans = question.split("-")
        TestAnswerDictionary[key] = ans.strip("\n")

#Option Dictionary for index and letter conversion
OptionDictionary = {0:"A", 1:"B", 2:"C", 3:"D"}

#File operation would be carried out at ./Exam_Papers/ Folder
examPaperPath = Path.cwd() / "Exam_Papers"
os.chdir(examPaperPath)


for x in range(35):
    #Shuffle options for each question
    for options in TestQuestionDictionary.values():
        random.shuffle(options)

    #Shuffle questions in the test paper
    shuffled_list = list(TestQuestionDictionary.items())
    random.shuffle(shuffled_list)

    #Writing Shuffled Test Paper
    with open(f"{x}.txt", "w") as file:
        questionNum = 1
        for question, option in shuffled_list:
            file.write(str(questionNum) + "," + question + "\n")
            file.write("A " + option[0]+ "\n")
            file.write("B " + option[1]+ "\n")
            file.write("C " + option[2]+ "\n")
            file.write("D " + option[3]+ "\n")
            questionNum += 1
    
    #Writing Shuffled Answer sheet 
    with open(f"{x}Answer.txt", "w") as answer:
        questionNum = 1
        for question, options in shuffled_list:
            answer.write(str(questionNum) + "," + question + " " + OptionDictionary[options.index(TestAnswerDictionary[question])] + "\n")
            questionNum += 1

print("35 randomized exam papers successfully generated.")