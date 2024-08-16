from element_symbols_data import data
import random

# indices consists of all the index numbers present in countries data
indices = [_ for _ in range(len(data))]
# dictionary to encode-decode each option
options = {0: 'a. ', 1: 'b. ', 2: 'c. ', 3: 'd. '}

def generate_options(ans):
    """
    This function generates random options for each question
    """
    choice_list = [0, 0, 0, 0]
    num = [0, 1, 2, 3]

    # assign one random choice to correct answer
    ans_index = random.randint(0, 3)
    choice_list[ans_index] = ans
    num.remove(ans_index)

    # and fill the remaining options with random symbols
    for j in num:
        random_index = random.choice(indices)
        other_options = data[random_index]["symbol"]
        while other_options == ans:
            # make sure that the randomly generated symbol is not equal to the correct answer
            random_index = random.choice(indices)
            other_options = data[random_index]["symbol"]
        choice_list[j] = other_options

    return ans_index, choice_list


def show_options(list_of_options):
    """
    This is how the options are presented to the user
    """
    for i in range(4):
        print(f"{options[i]}{list_of_options[i]}")

    print("\n")


def take_user_input():
    """
    This functions takes a valid input from the user
    and returns the index of user's answer
    """
    user = input('Select a/b/c/d : ').lower()

    if user == 'a':
        return 0
    elif user == 'b':
        return 1
    elif user == 'c':
        return 2
    elif user == 'd':
        return 3
    else:
        print('Please select a valid option')
        return take_user_input()


class Question:

    def __init__(self, i):
        """
        Defining attributes of Question class:
        question, answer, index of the answer, set of 4 options
        """
        self.question = f"What is the symbol of {data[i]['element']}?"
        self.answer = data[i]["symbol"]
        self.answer_index, self.options = generate_options(self.answer)
        self.score = 0

class Quiz:

    def __init__(self, q_list):
        """
        :param q_list: is a list that contains the question bank (instances of Question class)
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        """
        Presents the current question to the user,
        takes their input,
        checks the answer and tells the current score
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q{self.question_number}. {current_question.question} ")
        show_options(current_question.options)

        # Use the following command to show the correct answer on the screen
        # print(current_question.answer)

        user_answer = take_user_input()
        self.check_answer(user_answer, current_question.answer_index)
        print(f"The correct answer was {current_question.answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("=" * 50)
        print("\n")

    def check_answer(self, user_answer, correct_answer):
        """
        This method compares the user's answer with the correct one
        and calculates score
        """
        if user_answer == correct_answer:
            self.score += 1
            print(f"Yay! You've got it right!")
        else:
            print("Sorry! Wrong answer!")

    def still_has_questions(self):
        """
        Checks if there are more questions to be asked
        """
        total_questions = len(self.question_list)
        return self.question_number < total_questions

