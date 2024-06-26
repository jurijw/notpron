"""
Collection of utilities for use in solving the NOTPRON riddles. These include a myriad of methods to manipulate and decypher strings, as well as other helpful tools.
"""

# The standard English alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def invertChar(c):
    """Given a letter C in the alphabet, return the letter at the same index, given that the alphabet has been inverted."""
    index = ALPHABET.find(c)
    return ALPHABET[::-1][index]

def invert(string):
    """Given a STRING of characters, invert all characters that are part of the English alphabet. If other characters are present, such as '/' or ',' these are kept and not inverted."""
    output = ""
    for char in string:
        if char not in ALPHABET:
            output += char
        else:
            output += invertChar(char)
    return output

def caesar(string, shift=1):
    """Applies a Caesarian cypher to a STRING whereby each character in that string is shifted by an amount SHIFT. If a character is not present in the English alphabet, the cypher is not applied."""
    output = ""
    for char in string:
        if char not in ALPHABET:
            output += char
        else:
            index = ALPHABET.find(char)
            output += ALPHABET[(index + shift) % len(ALPHABET)]
    return output

def all_caesar(string):
    """Compute all possible caesar cyphers for a given STRING."""
    return [caesar(string, shift) for shift in range(26)]

from itertools import permutations
def permutations(string):
    """Returns an array containing all permuted strings variants of the input string"""
    return ["".join(perm) for perm in permutations(string)]

def select_chars_by_index(string, indexArray):
    """Returns the string formed by concatenating the characters of STRING found at each index in INDEXARRAY. Indexes starting from 1! (This is because, so far, notpron has always indexed starting from 1."""
    return "".join([string[i-1] for i in indexArray])

def select(stringArray, nestedIndexArray):
    """Returns an array of strings formed by applying selectCharsFromArrayByIndex to each string in STRINGARRAY, to each index array in NESTEDINDEXARRAY."""
    return [select_chars_by_index(string, indexArray) for string, indexArray in zip(stringArray, nestedIndexArray)]
