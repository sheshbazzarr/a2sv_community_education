from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k==0:
            for i in range(n):
                code[i]=0
            return code
        COPYCODE=code[:] # O(n) ---->>
         
        if k>0:
            for i in range(n):
                code[i]=sum(COPYCODE[(i+j)%n] for j in range(1,k+1))
        else:
            for i in range(n):
                code[i]=sum(COPYCODE[(i+j)%n] for j in range(k,0))
        return code

        # time complexity O(n)
        # space  0(1)
