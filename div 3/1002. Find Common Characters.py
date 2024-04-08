class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        random_count=[100]*26
        for s in words:
            current_count=[0]*26
            for c in s:
                c=ord(c)
                a=ord('a')
                current_count[c-a]+=1
            for c in range(26):
                total_count_bit=random_count[c]
                current_count_bit=current_count[c]
                random_count[c]=min(total_count_bit,current_count_bit)
                
        result=[]
        for c in range(26):
            for x in range(random_count[c]):
                result.append(chr(c+ord("a")))
        return result
