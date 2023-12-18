# Standard hangman game where one player submits a word and the other guesses it

# Guessing player receives a total amount of wrong chances equal to the length of the word + 2

# The guessing player is allowed a free chance to guess the entire word after each letter submission

# After all chances have been expended the game ends and a result is declared


class InvalidAnswerException(Exception):
    pass


def answerMaker():
    while True:
        try:    
            answer = str(input('\nPlease submit a word to be guessed: '))
            answer = answer.lower()
            answer = answer.strip()
            if len(answer.split()) > 1:
                raise InvalidAnswerException
            else:
                return answer
                break
        except InvalidAnswerException:
            print('Exception occurred: More than one word submitted, please try again')

#   Accepts a hint that is five words or less from the player     

def hintMaker():
    while True:
        try:
            hint = str(input('\nPlease submit a hint that is five words or less: '))
            if len(hint.split()) > 5:
                raise InvalidAnswerException
            else:
                return hint
                break
        except InvalidAnswerException:
            print('Exception occurred: More than five words were submitted, please try again')


def guessedWordMaker(word):
    guessedWord = ''
    for c in word:
        guessedWord = guessedWord + '_'
    return guessedWord
        


def getNextGuess():
    while True:
        try:
            guess = str(input('\nPlease submit a letter: '))
            guess = guess.lower()
            if len(guess) > 1 or not guess.isalpha():
                raise InvalidAnswerException
            else:
                return guess
                break
        except InvalidAnswerException:
            print('Exception occurred: Incorrect value submitted, please try again')

def solveEarly():
    choice = str(input('Would you like to try and guess? (Y , N): '))
    choice = choice.upper()
    if choice == 'Y':
        solve = str(input(f'\nPlease type your guess here: '))
        solve.lower()
        return solve , choice
    elif choice == 'N':
        solve = ''
        return solve , choice
    else:
        print('Invalid Choice')
        return solveEarly()
                
            
        

def hangmanGame():
    correctAnswer = answerMaker()
    hint = hintMaker()
    guessedWord = guessedWordMaker(correctAnswer)
    maximumGuesses = len(correctAnswer) + 2
    length = len(correctAnswer)
    totalGuesses = 0
    correctTrigger = 0
    guessList = []
    result = 'You Lose!'
    typedGuess = ''
    choice = 'N'

    while totalGuesses < maximumGuesses:
        print(f'\n{guessedWord}     You have {maximumGuesses - totalGuesses} chance(s) left!\n')
        if guessedWord == correctAnswer:
            result = 'You Win!'
            break
        solve , choice = solveEarly()
        if choice == 'Y':
            typedGuess = solve
            choice = 'N'
        if typedGuess == correctAnswer:
            result = 'You Win!'
            break
        currentGuess = getNextGuess()
        counter = 0
        correctTrigger = 0
        for c in correctAnswer:
            if currentGuess in guessList:
                break
            if c == currentGuess:
                guessedWord = guessedWord[0:counter] + c + guessedWord[counter+1:length]
                counter = counter + 1
                correctTrigger = correctTrigger + 1
            else:
                counter = counter + 1
        if correctTrigger < 1:
            totalGuesses = totalGuesses + 1
        guessList.append(currentGuess)
    
    print(f'\n{result}\n')

hangmanGame()



