# Level 20 of NOTPRON
hint = "xndrgarsennisennasen"

# The password hint when clicking the windows logo reads
# "don't mind the lead/pb". This could be an indication to
# ignore all the pencil writing on the page and focus on
# what is written in pen instead.

letters_in_pen = ["m", "kap", "tcs", "mb", "k", "q", "h"]
numbers_in_pen = [32, 64, 22.5, 69, 41, 94, 8202, 69, 213]

all_letters = "".join(letters_in_pen)

from itertools import permutations

# There are 12 letters in pen, meaning 12! permutations if permute by character. However, there are 7 distinct groupings of charactes (as far as I can tell) so only 7! possible permutations of the groupings.

# Compute all permutations of (grouped) letters
grouped_letter_permutations = ["".join(perm) for perm in permutations(letters_in_pen)]


