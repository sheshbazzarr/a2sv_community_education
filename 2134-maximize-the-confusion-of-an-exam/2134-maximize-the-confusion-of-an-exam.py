class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, maxChanges: int) -> int:
        # Find the max consecutive answers by turning 'F' to 'T' or 'T' to 'F'
        maxConsecutiveT = self.findMaxConsecutive(answerKey, maxChanges, 'T')
        maxConsecutiveF = self.findMaxConsecutive(answerKey, maxChanges, 'F')
        
        # Return the maximum of both cases (either maximizing 'T' or 'F')
        return max(maxConsecutiveT, maxConsecutiveF)

    def findMaxConsecutive(self, answerKey: str, maxChanges: int, target: str) -> int:
        maxConsecutive = -1
        length = len(answerKey)
        changesMade = 0
        leftPointer = 0

        # Use sliding window to check consecutive answers
        for rightPointer in range(length):
            # If the current character is not the target, increment the number of changes
            if answerKey[rightPointer] != target:
                changesMade += 1
            
            # If the number of changes exceeds maxChanges, adjust the left pointer
            while changesMade > maxChanges:
                if answerKey[leftPointer] != target:
                    changesMade -= 1
                leftPointer += 1
            
            # Update the maximum length of consecutive answers
            maxConsecutive = max(rightPointer - leftPointer + 1, maxConsecutive)
        
        return maxConsecutive
