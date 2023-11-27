from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
# question = Question()
question_bank = []
for ques in question_data:
    text = ques["text"]
    answer = ques["answer"]
    new_question = Question(text,answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():

    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was : {quiz.score} / {len(question_bank)} ")    