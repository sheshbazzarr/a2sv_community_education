class Solution:
    def binaryGap(self, n: int) -> int:
        binary_number =bin(n)[2:]
        positions =[i for i, bit in enumerate(binary_number) if bit=='1']
        if len(positions)<2:
            return 0
        max_ = 0
        for i in range(1, len(positions)):
            max_=max(max_,positions[i]-positions[i-1])
        return max_
