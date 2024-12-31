from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        total_length = len(words) * word_length
        word_count = defaultdict(int)

        # Count the frequency of each word in words
        for word in words:
            word_count[word] += 1

        result = []

        # Iterate through s in windows of size total_length
        for i in range(len(s) - total_length + 1):
            current_count = defaultdict(int)
            valid = True

            # Check each word in the current window
            for j in range(0, total_length, word_length):
                word = s[i + j:i + j + word_length]
                if word in word_count:
                    current_count[word] += 1
                    if current_count[word] > word_count[word]:
                        valid = False
                        break
                else:
                    valid = False
                    break

            # If the current window is valid, add the starting index to the result
            if valid:
                result.append(i)

        return result