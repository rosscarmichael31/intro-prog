# Name:
# MIT Username: 
# 6.S189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    #print('Enter play_hangman() to play a game of hangman!')
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()

# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------

# CONSTANTS
MAX_GUESSES = 6
MAX_WARNINGS = 3
VOWELS = ("a", "e", "i", "o", "u")

# GLOBAL VARIABLES 
#secret_word = get_word()
letters_guessed = []

# From part 3b:
def is_word_guessed(secret_word, letters_guessed):
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.

    >>> word_guessed("apple", ["e", "e", "l", "p", "p", "a"])
    True
    >>> word_guessed("apple", ["e", "i", "k", "p", "r", "s"])
    False
    '''

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
        continue
    return True



    # print(secret_word, letters_guessed)
    # for letter in letters_guessed:
    #     if letter in secret_word:
    #         next
    #     else:
    #         return False
    
    # return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    Prints a string that contains the word with a dash "-" in
    place of letters not guessed yet. 

    # >>> print_guessed("apple", ["e", "i", "k", "p", "r", "s"])
    # _ pp_ e
    # >>> print_guessed("apple", ["e", "e", "l", "p", "l", "a"])
    # apple
    '''
    output = ""
    for letter in secret_word:
        if letter in letters_guessed:
            output += letter
        else:
            output += "_ "
    
    return output

def get_available_letters(letters_guessed):
    """
    Return a string of available letters which can still be guessed.
    """
    return "".join([x for x in ascii_lowercase if x not in letters_guessed])

def unique_chars(string):
    """
    Return the number of unique characters in a string.
    """
    return len(set(string))


def play_hangman():
    # Actually play the hangman game

    mistakes_made = 0
    warnings = 0
    letters_guessed = []
    won = False

    print("Welcome to the game Hangman!")

    # secret_word  = get_word()
    secret_word = "else"

    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {MAX_WARNINGS} warnings left.")

    # Game loop
    while mistakes_made < MAX_GUESSES and not won:
        print("-------------")
        #print(f"You have {3-warnings} warnings left.")
        print(f"You have {MAX_GUESSES-mistakes_made} guesses left.")
        print(f"Availible letters: {get_available_letters(letters_guessed)}")

        guess = input("Please guess a letter: ")

        # Deal with warnings if necessary
        # TODO: Make helper function?
        if not guess.isalpha():
            if warnings >= MAX_WARNINGS:
                print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
                mistakes_made += 1
                continue 

            warnings += 1
            print(f"Oops! That is not a valid letter. You have {MAX_WARNINGS-warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            continue
        
        if guess in letters_guessed:
            if warnings >= MAX_WARNINGS:
                print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
                mistakes_made += 1
                continue

            warnings += 1
            print(f"Oops! You've already guessed that letter. You have {MAX_WARNINGS-warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            continue 


        # Output if guess is correct ot not
        # Add letter to guessed letters
        letters_guessed.append(guess.lower())
        if guess in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")

            if is_word_guessed(secret_word, letters_guessed):
                won = True
                continue


        elif guess in VOWELS:
            mistakes_made += 2
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")

        else:
            mistakes_made += 1
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")


    if won:
        total_score = (MAX_GUESSES - mistakes_made) * unique_chars(secret_word)
        print("------------")
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {total_score}")
    
    else:
        print("-----------")
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

play_hangman()



