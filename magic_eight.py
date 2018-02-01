<<<<<<< HEAD
def question:
    x=input("What is your question?")
=======
import random

def question:
    x=input("What is your question?")

    answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
    "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes"]

    random_answer = random.choice(answers)
    return random_answer
>>>>>>> add_questions2
