import random

# stałe
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

maxGuesses = len(HANGMAN) - 1
WORDS = ("developer", "programowanie", "pies", "książka", "wisielec")

word = random.choice(WORDS)

guessed = "-" * len(word)
missed = 0
usedLetters = []

print("Gra w wisielca")
print("Zaczynamy")
print(HANGMAN[missed])

while missed < maxGuesses and guessed.lower() != word:
    letter = input("Wybierz literę: ")
    usedLetters.append(letter)
    print("Użyte litery: ", usedLetters)
    print(guessed)
    if letter in word:
        print("Zgadłeś literę")
        newWord=""
        for i in range(len(word)):
            if letter == word[i]:
                newWord+=letter
            else:
                newWord+=guessed[i]
        guessed = newWord

    else:
        print("Nie zgadłeś")
        missed+=1
        print(HANGMAN[missed])

    giveAnswer = input("Chcesz podac całe słowo?(Y/N): ")

    if giveAnswer == "Y" or giveAnswer == "y":
        wholeWord = input("Podaj słowo: ")
        if wholeWord == word:
            print("Hurra zgadłeś!")
            break
        else:
            print("Nie zgadłeś, próbuj dalej!")

