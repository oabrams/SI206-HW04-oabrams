import random

def question():
    x=input("What is your question?")

    answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
    "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now",
    "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good" "Very doubtful"]

    while x != "quit":
        if x[-1]!="?":
            print( "I'm sorry, I can only answer questions.")
        else:
            random_answer = random.choice(answers)
            print(random_answer)
        x=input("What is your question?")

question()
