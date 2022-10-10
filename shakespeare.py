"""
Data Structures - Shakespeare

6/10/22
"""
from collections import Counter

text = open("shakespeare.txt")
shakes = open("shakespeare.txt")
text = shakes.read().lower().replace("-", " ").replace(",", " ").replace(".", " ") \
.replace("?", " ").replace("!", " ").replace(":"," ").replace(";", " ").split()

# Longest word
longest_word = sorted(text, key=len)[-1]
print(longest_word, len(longest_word))

# Longest palindrome
palindromes = []
for word in text:
    if word == word[::-1]:
        palindromes.append(word)

longest_palindrome = sorted(palindromes, key=len)[-1]
print(longest_palindrome, len(longest_palindrome))

# Most common word
c = Counter(text)
print(c.most_common(3))

# How many different words
print(len(set(text)))


###
punctuation = {"!", "?", ":", ";", "-", ",", "."}
unique = {word.lower() for word in text if word not in punctuation}







