from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        COPYCODE=[0]*n
        if k==0:
            return COPYCODE 
         
        if k>0:
            for i in range(n):
                COPYCODE[i]=sum(code[(i+j)%n] for j in range(1,k+1))
        else:
            for i in range(n):
                COPYCODE[i]=sum(code[(i+j)%n] for j in range(k,0))
        return COPYCODE

        # time complexity O(n)
        # space  0(N)
