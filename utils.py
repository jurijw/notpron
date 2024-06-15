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

