class Solution:
    def smallestNumber(self, num: int) -> int:
        s = sorted(str(abs(num)))
        if num <= 0:
            return -int(''.join(s[::-1]))
        i = next(i for i,num in enumerate(s) if num > '0')
        s[i], s[0] = s[0], s[i]
        return int(''.join(s))
