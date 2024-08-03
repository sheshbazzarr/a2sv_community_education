class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def compareCounter(a, b):
            for c in a:
                if a[c] != b[c]:
                    return False
            return True

        ret, n = [], len(p)
        if len(s) < n:
            return ret
        counterP, counterS, ret = Counter(p), Counter(s[:n]), []

        for i in range(len(s) - n + 1):
            if i > 0:
                counterS[s[i - 1]] -= 1
                counterS[s[i + n - 1]] += 1
            if compareCounter(counterS, counterP):
                ret.append(i)
        return ret