class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        string_length =len(s)
        for substring_length in range(1, string_length//2+1):
            if string_length % substring_length==0:
                candidate_substring =s[:substring_length]

                repeat_count = string_length//substring_length

                reconstructed_string =candidate_substring * repeat_count

                if reconstructed_string ==s:
                    return True
        return False



