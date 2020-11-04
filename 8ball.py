import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'it is decidedly so'
    elif answerNumber == 3:
        return 'YES'
    elif answerNumber == 4:
        return 'reply hazy try again'
    elif answerNumber == 5:
        return 'ask again'
    elif answerNumber == 6:
        return 'concentrate and ask again'
    elif answerNumber == 7:
        return 'my reply is no'
    elif answerNumber == 8:
        return 'outlook not so good'
    elif answerNumber == 9:
        return 'very doubtful'
r=random.randint(1,9)
fortune=getAnswer(r)
print(fortune)
