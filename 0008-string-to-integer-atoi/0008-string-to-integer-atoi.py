class Solution:
    def myAtoi(self, s: str) -> int:
        sign =['-','+']
        s = s.split()
        if len(s)==0:
            return 0
        s = s[0]
        res = ''
        for i ,val in enumerate(s):
            if i ==0:
                if (s[i] in sign or s[i].isdigit()):
                    res +=s[i]
                else:
                    break
            else:
                if s[i].isdigit():
                    res +=s[i]
                else:
                    break
        try:
            nums = int(res)
        except:
            return 0
        if nums > 2**31-1:
            return 2**31-1
        if nums < -2**31:
            return -2**31
        return nums