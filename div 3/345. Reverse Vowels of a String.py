class Solution:
   def reverseVowels(self, s: str) -> str:
        if len(s) == 0:
            return s
        L = 0
        R = len(s) - 1
        list_ = list(s)
        vowels = set(['a', 'e', 'i', 'u', 'o'])
        while L < R:
            if list_[L].lower() not in vowels:
                L += 1
            elif list_[R].lower() not in vowels:
                R -= 1
            else:
                list_[L], list_[R] = list_[R], list_[L]
                R -= 1
                L += 1
        return "".join(list_)

                
                
            
        
