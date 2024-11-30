class Solution:
    def minLength(self, s: str) -> int:
        result = []
        for char in s:
            result.append(char)

            if len(result)>=2 and (result[-2:]==['A','B'] or result[-2:]==['C','D']):
                result.pop()
                result.pop()
        return len(result)

                

