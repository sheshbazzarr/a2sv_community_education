# Read the input strings
s = input()
t = input()

# Initialize pointers and the number of moves
ptr_s = 0
ptr_t = 0
moves = 0

# Iterate through the strings until one or both become empty
while ptr_s < len(s) and ptr_t < len(t):
    # If the characters at the current positions are equal
    if s[ptr_s] == t[ptr_t]:
        ptr_s += 1
        ptr_t += 1
    else:
        # Increment the number of moves and move the pointer of the string with the larger character
        moves += 1
        if s[ptr_s] < t[ptr_t]:
            ptr_s += 1
        else:
            ptr_t += 1

# Add the remaining characters and the number of moves if any string is not empty
moves += len(s) - ptr_s + len(t) - ptr_t

# Output the fewest number of moves required
print(moves)
