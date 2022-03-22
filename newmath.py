#!/usr/bin/python3
import random
import sys

class Question:

    def __init__(self, question, amount, *args, **kwargs):
        self.amount = amount
        self.kwargs = kwargs 
        self.args = args
        self.question = question

    def prompt(self):
        for i in range(self.amount):
            self.question(*self.args, **self.kwargs)


def user_answer(prompt='',):
    try:
        answer = input(f"{prompt}: ")
    except EOFError:
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)
    return answer


def square_to_ten():
    while True:
        answers = user_answer("1² to 10²").split(' ')

        isalpha = lambda l : bool([i for i in l if i.isalpha()])
        if isalpha(answers) == True:
            print("Huh?")
            continue

        if len(answers) != 10:
            print(f"Wong amount of numbers, '{len(answers)}', must be 10")
            continue

        answers = [int(i) for i in answers]
        answers.extend([i**2 for i in range(1,11)])
        if len(set(answers)) != 10:
            print("Wrong!")
        else:
            print("Correct!")
            break


def random_add(min=1, max=50):
    addends = [
            random.randint(min, max),
            random.randint(min, max),
    ]
    while True:
        answer = sum(addends)
        prompt = ' + '.join([str(i) for i in addends])
        user = user_answer(prompt).split(' ')[0]

        if user.isalpha() == True:
            print("Huh?")
            continue

        if int(user) != answer:
            print("Wrong!")
        else:
            print("Correct!")
            break
        

def main():

    questions = [
            Question(square_to_ten, amount=1),
            Question(random_add, amount=3, min=1, max=100),
            ]

    for q in questions:
        q.prompt()


if __name__ == "__main__":
    main()
