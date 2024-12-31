from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)  # Convert wordList to a set for O(1) lookups
        queue = deque([(beginWord, 1)])  # Queue stores (current_word, current_length)
        visited = set(beginWord)  # Track visited words

        while queue:
            current_word, length = queue.popleft()

            # Check all possible transformations
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == current_word[i]:
                        continue  # Skip the same character
                    new_word = current_word[:i] + c + current_word[i+1:]

                    if new_word == endWord:
                        return length + 1  # Found the shortest path

                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))

        return 0  # No transformation sequence found