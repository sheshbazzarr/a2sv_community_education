class Solution:
    def countSeniors(self, details: List[str]) -> int:
        sinor=0
        for i in details:
            if int(i[11]+i[12])>60:
                sinor+=1
        return sinor