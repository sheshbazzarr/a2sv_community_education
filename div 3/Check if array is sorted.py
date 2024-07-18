#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        # code here
        
        for i in range(len(arr)):
            if arr[i]>arr[i+1]:
                return False
            else:
                continue
        return True
                

#{ 
 # Driver Code Starts
# Importing necessary modules
import sys
from typing import List

# Main function
if __name__ == "__main__":
    input = sys.stdin.read().strip().split("\n")
    t = int(input[0])
    index = 1
    solution = Solution()

    for _ in range(t):
        line = list(map(int, input[index].strip().split()))
        index += 1
        ans = solution.arraySortedOrNot(line)
        print("true" if ans else "false")
# } Driver Code Ends
