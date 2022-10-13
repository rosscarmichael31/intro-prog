#!/usr/bin/env python3

"""
============
Hangman Game
============

Ross Carmichael
11/10/22

"""
from random import randrange
from string import *
import os


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
    print("  ", len(wordlist), "words loaded.\n")

    return wordlist


def get_word(words_dict):
    """
    Returns a random word from the word list
    """
    word = words_dict[randrange(0, len(words_dict))]
    return word


def is_word_guessed(secret_word, letters_guessed):
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.

    >>> is_word_guessed("apple", ["e", "e", "l", "p", "p", "a"])
    True
    >>> is_word_guessed("apple", ["e", "i", "k", "p", "r", "s"])
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

    # >>> get_guessed_word("apple", ["e", "i", "k", "p", "r", "s"])
    # _ pp_ e
    # >>> get_guessed_word("apple", ["e", "e", "l", "p", "l", "a"])
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


def match_with_gaps(my_word, other_word, letters_guessed):
    """
    my_word => guessed word with _ _
    other_word => normal word (secret_word)

    >>> match_with_gaps("te_ t", "tact", letters_guessed)
    False
    >>> match_with_gaps("a_ _ le", "banana", letters_guessed)
    False
    >>> match_with_gaps("a_ _ le", "apple", letters_guessed)
    True
    >>> match_with_gaps("a_ ple", "apple", letters_guessed)
    False
    """
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False

    for i in range(len(my_word)):
        if my_word[i] == "_":
            if other_word[i] in letters_guessed:
                return False
            continue
        elif my_word[i] != other_word[i]:
            return False

    return True


def show_possible_matches(my_word, words_dict, letters_guessed):
    """
    my_word => guessed word with _ _
    """
    matches = [word for word in words_dict if match_with_gaps(
        my_word, word, letters_guessed)]

    return matches if matches else "Sorry, no matches found"


def play_hangman(secret_word, words_dict):
    """
    Contains the main logic behind the hangman game.
    """
    mistakes_made = 0
    warnings = 0
    letters_guessed = []
    won = False

    print("============================")
    print("Welcome to the game Hangman!")
    print("============================\n")

    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {MAX_WARNINGS} warnings left.")

    # Game loop
    while mistakes_made < MAX_GUESSES and not won:
        print("-------------")
        print(f"You have {MAX_GUESSES-mistakes_made} guesses left.")
        print(f"Availible letters: {get_available_letters(letters_guessed)}")

        guess = input("Please guess a letter: ")
        os.system("clear")

        # Display hints
        if guess == "*":
            matches = show_possible_matches(get_guessed_word(
                secret_word, letters_guessed), words_dict, letters_guessed)
            print(f"Possible word matches are: \n {' '.join(matches)}")
            print(get_guessed_word(secret_word, letters_guessed))
            continue

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


# CONSTANTS
WORDLIST_FILENAME = "words.txt"
MAX_GUESSES = 7
MAX_WARNINGS = 3
VOWELS = ("a", "e", "i", "o", "u")


def main():
    # Load available words
    words_dict = load_words()

    # Choose a secret word
    secret_word = get_word(words_dict)

    play_hangman(secret_word, words_dict)


if __name__ == "__main__":
    main()
