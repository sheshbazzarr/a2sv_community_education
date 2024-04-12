class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_list=[]
        for ent in nums:
            str_list+=[str(ent)]
        L=len(str_list)
        for sLw in range(L):
            for fAs in range(sLw+1,L):
                ascend=str_list[sLw]+str_list[fAs]
                descend=str_list[fAs]+str_list[sLw]
                
                if ascend > descend:
                    continue
                else:
                    str_list[sLw],str_list[fAs]=str_list[fAs],str_list[sLw]
        Number= "".join(str_list)
        if int(Number)==0:
            return '0'
        return Number
