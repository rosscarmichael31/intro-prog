"""
Hangman Game
============

Ross Carmichael
11/10/22

"""

from random import randrange
from string import *


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
    print("  ", len(wordlist), "words loaded.")

    return wordlist


def get_word():
    """
    Returns a random word from the word list
    """
    word = words_dict[randrange(0, len(words_dict))]
    return word


# Load words from file
WORDLIST_FILENAME = "words.txt"
words_dict = load_words()

# CONSTANTS
MAX_GUESSES = 6
MAX_WARNINGS = 3
VOWELS = ("a", "e", "i", "o", "u")


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


def winning_message(mistakes_made, secret_word):
    """
    Display a winning message to the player with their score.
    """

    def get_total_score():
        """
        Return the total score if the player wins the game.
        """
        return (MAX_GUESSES - mistakes_made) * unique_chars(secret_word)

    print("------------")
    print("Congratulations, you won!")
    print(
        f"Your total score for this game is: {get_total_score()}")


def losing_message(secret_word):
    """
    Display a losing message to the player, revealing the secret word.
    """
    print("-----------")
    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


def play_hangman(secret_word):
    """
    Contains the main logic behind the hangman game.
    """
    mistakes_made = 0
    warnings = 0
    letters_guessed = []
    won = False

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {MAX_WARNINGS} warnings left.")

    # Game loop
    while mistakes_made < MAX_GUESSES and not won:
        print("-------------")
        print(f"You have {MAX_GUESSES-mistakes_made} guesses left.")
        print(f"Availible letters: {get_available_letters(letters_guessed)}")

        guess = input("Please guess a letter: ")

        # Deal with warnings if necessary
        if not guess.isalpha():
            if warnings >= MAX_WARNINGS:
                print(
                    f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
                mistakes_made += 1
                continue

            warnings += 1
            print(
                f"Oops! That is not a valid letter. You have {MAX_WARNINGS-warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            continue

        if guess in letters_guessed:
            if warnings >= MAX_WARNINGS:
                print(
                    f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
                mistakes_made += 1
                continue

            warnings += 1
            print(
                f"Oops! You've already guessed that letter. You have {MAX_WARNINGS-warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            continue

        # Append choice to guessed letters
        letters_guessed.append(guess.lower())

        # Output if guess is correct ot not
        if guess in secret_word:
            print(
                f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")

            if is_word_guessed(secret_word, letters_guessed):
                won = True
                continue

        elif guess in VOWELS:
            mistakes_made += 2
            print(
                f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")

        else:
            mistakes_made += 1
            print(
                f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")

    winning_message(
        mistakes_made, secret_word) if won else losing_message(secret_word)


def main():
    secret_word = get_word()
    play_hangman(secret_word)


if __name__ == "__main__":
    main()
