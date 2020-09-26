"""
Suppose there are two lists - one contains questions and another contains a list of 4 possible answers for each question.
WAP to generate a list that contains lists of question and its 4 possible answers
"""

q = ["What is a star?", "What is a planet?", "What is a satellite?"]

a = ["It is a toy", "It is a car", "It is a bike", "It is a burning ball of gas",
     "It is a rotating rock revolving around star", "It is a ship", "It is a plane", "It is a burning ball of joker",
     "It is a rotating rock revolving around planet", "It is a car", "It is a rabbit", "It is a burning ball of lion"]

merge_list = [*q, *a]
print(merge_list)