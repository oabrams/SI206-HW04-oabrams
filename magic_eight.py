
def question:
    x=input("What is your question?")
    while x != "quit":
        x=input("What is your question?")
        if x[-1]!="?":
            return "I'm sorry, I can only answer questions."
