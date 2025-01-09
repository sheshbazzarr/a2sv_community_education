class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:].zfill(32)
        reveresed_binary =binary[::-1]

        return int(reveresed_binary,2)