from Score import *


game = ""
def welcome(name):
    print('Hello ' + name + ' and welcome to the World of Games (WoG). \nHere you can find many cool games to play.\n\n\n')
def load_game(name):
    game = int(input("Please choose a game to play: \n"
                 "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                 "2. Guess Game - guess a number and see if you chose like the computer\n"
                 "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
                 "4. Print Plyer Scores http://127.0.0.1:5000 or http://127.0.0.1:5000/scores/\n"
                 ":"))

    difficulty = input("\n\n\nPlease choose game difficulty from 1 to 5: ")
    score = ((int(difficulty) * 3) + 5)
    # match case
    match game:
        # pattern 1
        case 1:
            print("\n\n\nYou have choose to play: Memory Game\ndifficulty level: " + difficulty)
            from MemoryGame import play
            #play(difficulty,name)
            if play(difficulty,name):
                updatePlayerDatatxt(score)
                updatePlayerData(name, "Memory Game", score)
            else:
                score = 0
                updatePlayerDatatxt(score)
                updatePlayerData(name, "Memory Game", score)
        # pattern 2
        case 2:
            print("You have choose to play: Guess Game\ndifficulty level: " + difficulty)
            print("\n\n\n\nlets Play the Guess Game")
            from GuessGame import play
            play(difficulty,name)
            updatePlayerDatatxt(score)
            updatePlayerData(name, "Guess Game", score)
        # pattern 3
        case 3:
            print("You have choose to play: Currency Roulette\ndifficulty level: " + difficulty)
            print("\n\n\n\nlets Play the Currency Roulette Game")
            from CurrencyRouletteGame import play
            play(difficulty, name)
            updatePlayerDatatxt(score)
            updatePlayerData(name, "Currency Roulette", score)
        # default pattern
        case _:
            print("Game option should be between 1 and 3")