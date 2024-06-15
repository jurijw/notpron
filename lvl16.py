"""
Clues: 
# = ellwll/hrnkov/proo/...
invert az
title: resume
url: /zoo/mznvh

The watch in level 4 is no longer lit up!
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"

def invert(c):
    """Given a letter C in the alphabet, return the letter at the same index, given that the alphabet has been inverted."""
    index = alphabet.find(c)
    return alphabet[::-1][index]

def invertString(string):
    output = ""
    for char in string:
        if char not in alphabet:
            output += char
        else:
            output += invert(char)
    return output

# Attempt to invert the url and first clue, alphabetically.
url = "zoo/mznvh"
url_hint = "ellwll/hrnkov/proo/..."

# Split url
jumbles = url_hint.split("/")[:-1]
unjumbled = [invertString(s) for s in jumbles]

# The unjumbled words are "voodoo", "simple", and "kill", which are the usernames to levels 4, 5, and 6, respectively.
print(unjumbled)

# Attempt to read all usernames, passwords, and urls, into lists.

# Import markdown document, with all found username/password/url combinations.
info = ""
with open("info.md", 'r') as f:
    for line in f:
        info += line 

# Perform RegEx search to determine username/password/url for each level.
import re 

url_pattern = r"url:\s+(\S+)"
username_pattern = r"username:\s+(\S+)"
password_pattern = r"password:\s+(\S+)"

urls = re.findall(url_pattern, info)
usernames = re.findall(username_pattern, info)
passwords = re.findall(password_pattern, info)

# Create a dictionary with all the information gathered thusfar.
info_list = []

for i in range(len(urls)):
    level_info = {}
    level_info["url"] = urls[i]
    level_info["username"] = usernames[i]
    level_info["password"] = passwords[i]
    info_list.append(level_info) 


# Create a dataframe containing all information found thusfar.
import pandas as pd

df = pd.DataFrame(info_list)

# Based on the hint "# = ellwll/hrnkov/proo/..." and the fact that inverting these strings corresponds to the first three usernames, we create a url extension here with all found usernames.

filtered_usernames = [un for un in usernames if un != "n/a"]
usernames_url = "/".join(filtered_usernames)
jumbled_usernames_url = "/".join([invertString(s) for s in filtered_usernames])
print(usernames_url)
print(jumbled_usernames_url)

# Attempt to invert everything relating to a given level
def invertAll(level_index):
    print("url: " + invertString(info_list[level_index - 1]["url"].split("/notpron/")[1]))
    print("user: " + invertString(info_list[level_index - 1]["username"]))
    print("pass: " + invertString(info_list[level_index - 1]["password"]))


# This section deals with interpretting the grid of numbers given in level 16.
import numpy as np

arr = np.array([[0,0,0,4],
               [5,3,0,0],
               [5,0,1,1],
               [1,2,1,None]])


# Assuming that the pictures with 0s don't count, the username and password mayy be split between the pictures with #s and those without.

# sharp_levels = (5, 6, 8, 11)
# non_sharp_levels = (4, 9, 12, 13, 14, 15)
# 
# sharp_numbers = (5, 3, 2, 1)
# non_sharp_numbers = (4, 5, 1, 1, 2, 1)
# 
# un_string_sharp = ""
# pw_string_sharp = ""
# for num, lvl in zip(sharp_numbers, sharp_levels):
#     un_string_sharp += usernames[lvl - 1][num]
#     pw_string_sharp += passwords[lvl - 1][num]
# 
# un_string_non_sharp = ""
# pw_string_non_sharp = ""
# for num, lvl in zip(non_sharp_numbers, non_sharp_levels):
#     un_string_non_sharp += usernames[lvl - 1][num]
#     pw_string_non_sharp += passwords[lvl - 1][num]
# 
# print("Sharp cypher: ")
# print("Sampling from usernames: " + un_string_sharp)
# print("Sampling from passwords: " + pw_string_sharp)
# 
# print("Non sharp cypher: ")
# print("Sampling from usernames: " + un_string_non_sharp)
# print("Sampling from passwords: " + pw_string_non_sharp)

# This did not work...

# What finally did work was taking the ith character of every level's username which had a non-zero number in the grid. The levels which had #s, had to have the character inverted.


# Everything past this point is working on level 20. I am using this file until I refactor all the useful utilities into a separate one.
# Caesar cypher
def caesar(string, shift=1):
    output = ""
    for char in string:
        index = alphabet.find(char)
        output += alphabet[(index + shift) % len(alphabet)]
    return output

jumble = "xndrgarsennisennasen"

# Apply all possible Caesar cyphers to the mysterious string.
for i in range(len(alphabet)):
    print(caesar(jumble, shift=i))


