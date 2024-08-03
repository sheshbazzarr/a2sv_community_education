class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ans = []
        # Frequency arrays
        arr1 = [0] * 26
        arr2 = [0] * 26
        n, m = len(s), len(p)

        if m > n:
            return ans

        # First window
        for i in range(m):
            arr1[ord(p[i]) - ord('a')] += 1
            arr2[ord(s[i]) - ord('a')] += 1

        if arr1 == arr2:
            ans.append(0)

        # Subsequent windows
        for i in range(m, n):
            arr2[ord(s[i]) - ord('a')] += 1
            arr2[ord(s[i - m]) - ord('a')] -= 1

            if arr1 == arr2:
                ans.append(i - m + 1)

        return ans

