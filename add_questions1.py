import random

def question:
    x=input("What is your question?")

    answers=["Reply hazy try again", "Ask again later", "Better not tell you now",
    "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good" "Very doubtful"]

    for item in answers:
        random_answer = random.choice(answers)
        return random_answer
