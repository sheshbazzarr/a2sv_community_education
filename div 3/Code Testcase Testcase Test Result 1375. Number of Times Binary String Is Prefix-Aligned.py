class Solution:
      def numTimesAllBlue(self, flips: List[int]) -> int:
            s=set()
            n,m=0,0
            output=0
            for n in flips:
                s.add(n)
                m=max(n,m)
                if len(s)==m:
                    output+=1
            return output

