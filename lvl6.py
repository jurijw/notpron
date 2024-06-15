# Notpron Level 6
# Idea is to interpret the puzzle input as ASCII 
# or as indexing the alphabet directly
letters = "abcdefghijklmnopqrstuvwxyz"

puzzle = "108 105 108 107 101 122 111 110"

# Interpret every integer as the correspondingly indexed letter of the alphabet.
output = ""
for char in puzzle:
    if char != " ":
        output += letters[int(char)]
    else:
        output += " "

print(output)

# Interpret every three digit number as an ASCII code.
print([chr(int(num)) for num in puzzle.split(" ")])

