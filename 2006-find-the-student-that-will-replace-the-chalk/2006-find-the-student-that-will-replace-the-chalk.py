class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total=sum(chalk)
        full_cycles=k//total
        k-=full_cycles*total

        for i,x in enumerate(chalk):
            k-=x
            if k<0:
                return i
        assert(False)