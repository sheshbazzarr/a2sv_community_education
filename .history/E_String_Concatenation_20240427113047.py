# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read input
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    
    # Initialize the output binary string
    output = ''
    
    # Iterate through each string
    for i in range(n):
        # Initialize flag to check if substring is found
        found = False
        
        # Iterate through all possible substrings
        for j in range(1, len(strings[i])):
            # Check if the current substring exists in the list
            if strings[i][:j] in strings or strings[i][j:] in strings:
                found = True
                break
        
        # Append the corresponding bit to the output binary string
        output += '1' if found else '0'
    
    # Output the binary string for the current test case
    print(output)
#expected ouput is 
10100
011
10100101

the recived output :
10100
011
10100101