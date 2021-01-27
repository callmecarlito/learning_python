#Udemy - 2021 Complete Python Bootcamp From Zero to Hero in Python
#Lecture 47
#Compartmentalizing functions in a program
from random import shuffle

def shuffle_list(game_cups):
    shuffle(game_cups)
    return game_cups

def player_guess():
    options = ['0', '1', '2']
    guess = ''
    while guess not in options:
        guess = input("Pick your cup (0, 1, or 2): ")
    #user input always returned as string, so you need to cast it
    return int(guess)  

def check_guess(cups, players_cup):
    if cups[players_cup] == '0':
        print("You guessed right!")
    else:
        print("Sorry, maybe next time!")
    print(cups)

if __name__ == "__main__":
    #Initialize list
    cups = ['0', ' ', ' ']

    #Shuffle list
    shuffled_cups = shuffle_list(cups)

    #User guess
    players_cup = player_guess()

    #Checks user guess
    check_guess(shuffled_cups, players_cup)




