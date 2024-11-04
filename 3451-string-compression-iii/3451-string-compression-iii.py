class Solution:
    def compressedString(self, word: str) -> str:
        compress = []
        i = 0
        while i<len(word):
            count=1
            while i+count<len(word)  and word[i]==word[count+i] and count<9:
                count+=1
            compress.append(f'{count}{word[i]}')
            i+=count
        return ''.join(compress)
