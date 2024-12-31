from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        if endWord not in wordList:
            return []

        wordSet = set(wordList)  # Convert wordList to a set for O(1) lookups
        wordSet.add(beginWord)

        # Build a graph of possible transformations
        graph = defaultdict(list)
        for word in wordSet:
            for i in range(len(word)):
                wildcard = word[:i] + '*' + word[i+1:]
                graph[wildcard].append(word)

        # BFS to find the shortest distance and build the parent map
        parent = defaultdict(list)
        distance = {beginWord: 0}
        queue = deque([beginWord])

        while queue:
            current = queue.popleft()
            if current == endWord:
                break

            for i in range(len(current)):
                wildcard = current[:i] + '*' + current[i+1:]
                for neighbor in graph[wildcard]:
                    if neighbor not in distance:
                        distance[neighbor] = distance[current] + 1
                        parent[neighbor].append(current)
                        queue.append(neighbor)
                    elif distance[neighbor] == distance[current] + 1:
                        parent[neighbor].append(current)

        # Backtracking to reconstruct all shortest paths
        result = []
        self.backtrack(endWord, beginWord, parent, [endWord], result)
        return result

    def backtrack(self, current: str, beginWord: str, parent: dict, path: list, result: list):
        if current == beginWord:
            result.append(path[::-1])  # Reverse the path to get the correct order
            return

        for p in parent[current]:
            self.backtrack(p, beginWord, parent, path + [p], result)