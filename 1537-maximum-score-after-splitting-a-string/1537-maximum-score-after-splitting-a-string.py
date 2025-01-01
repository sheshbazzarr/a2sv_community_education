class Solution:
    def maxScore(self, s: str) -> int:
        total_ones =s.count('1')
        max_score = 0
        zeros = 0
        ones = total_ones
        for i in range(len(s)-1):
            if s[i]=='0':
                zeros +=1
            else:
                ones-=1
            current_score =zeros+ones
            if current_score>max_score:
                max_score =current_score
        return max_score