from question_list import quiz
from question import Question
from question_master import QuestionMaster

question_bank = []
for question in quiz:
    question_bank.append(Question(question["question"],question["answer"]))

question_master=QuestionMaster(q_list=question_bank)


question_master=QuestionMaster(q_list=question_bank)
question_master.start_quiz()