from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

# for i in range(len(question_data)):
    #question_bank.append(question_data[i]['text'])
# print(question_bank)

for question in question_data:
    ques_text = question['text']
    ans_text=question['answer']
    new_ques= Question(ques_text, ans_text)
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("****** Congratulations, you've reached the end of the game *****")
print(f"Your final Score is: {quiz.score}")
