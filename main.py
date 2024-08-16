import random
from quiz_code import Question, Quiz, indices
from art import logo

print(logo)
print("Welcome to the Quiz Game!\n")

# set the number of questions you want in the quiz here
num_of_questions = 15

# randomly select indices from countries data
# to get random questions every time you run the code
index_num = random.sample(indices, num_of_questions)

question_bank = []

# prepare questions and append to question_bank
for i in index_num:
    # for each index, create a Question instance
    new_question = Question(i)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Congratulations! You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
