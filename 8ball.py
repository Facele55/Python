import random


def get_answer(answer_number: int):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'YES'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'aAsk again'
    elif answer_number == 6:
        return 'Concentrate and ask again'
    elif answer_number == 7:
        return 'My reply is no'
    elif answer_number == 8:
        return 'Outlook not so good'
    else:
        return 'Very Doubtful'


if __name__ == "__main__":
    r = random.randint(1, 9)
    fortune = get_answer(r)
    print(fortune)
