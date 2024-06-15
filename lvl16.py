"""
Clues: 
# = ellwll/hrnkov/proo/...
invert az
title: resume
url: /zoo/mznvh
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"

def invert(c):
    """Given a letter C in the alphabet, return the letter at the same index, given that the alphabet has been inverted."""
    index = alphabet.find(c)
    return alphabet[::-1][index]

def invertString(string):
    output = ""
    for char in string:
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

# This section deals with interpretting the grid of numbers given in level 16.
import numpy as np

arr = np.array([[0,0,0,4],
               [5,3,0,0],
               [5,0,1,1],
               [1,2,1,None]])

