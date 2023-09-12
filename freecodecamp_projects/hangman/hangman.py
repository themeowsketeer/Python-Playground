import json
import random
import string

dataDict = {}

dataJSON = open('words.json')
dataDict = json.load(dataJSON)
data = dataDict['data']

def get_valid_single_word(data):
    chosen = random.choice(data)
    while '-' in chosen or ' ' in chosen:
        chosen = random.choice(data)
    return chosen

def hangman_main():
    chosen = get_valid_single_word(data)
    # print(f'(For debug only) Given word: {chosen}')
    chosenLetters = set(chosen)
    totalToGuess = len(chosenLetters)
    alphabet = set(string.ascii_lowercase)
    usedLetters = set()
    incorrectChance = 10
    print(f'Choose wisely. You have {incorrectChance} lives. The word has {totalToGuess} unique letters')
    while (len(chosenLetters) > 0 and incorrectChance > 0):
        print(f'Used letters: {usedLetters}')
        print(f'Left fault chance to guess: {incorrectChance}')
        userInput = input('Guess a letter: ').lower()
        if (userInput in alphabet - usedLetters):
            usedLetters.add(userInput)
            if (userInput in chosenLetters):
                chosenLetters.remove(userInput)
                print("Correct word.")
            else:
                print("Incorrect")
                incorrectChance -= 1
        elif (userInput in usedLetters):
            print('Used letter')
            incorrectChance -= 1
        else:
            print('Incorrect format')
    if (incorrectChance == 0):
        print(f'You failed. The correct word is {chosen}.')
        print(f'You successfully guessed {totalToGuess - len(chosenLetters)} out of {totalToGuess}')
    else:
        print(f'You won. You have {incorrectChance} left')
        print(f'The given word is {chosen}.')

print(hangman_main())