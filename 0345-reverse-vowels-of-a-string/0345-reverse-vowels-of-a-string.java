class Solution {
    public String reverseVowels(String s) {
        int n = s.length();
        char ch[] = s.toCharArray();
        int start = 0;
        int end = s.length() - 1;

        while (start < end) {
            // Move start pointer forward if not a vowel
            if (!isVowel(ch[start])) {
                start++;
            }
            // Move end pointer backward if not a vowel
            else if (!isVowel(ch[end])) {
                end--;
            }
            // Swap vowels
            else {
                char temp = ch[start];
                ch[start] = ch[end];
                ch[end] = temp;
                start++;
                end--;
            }
        }

        return String.valueOf(ch); // Return after the loop is done
    }

    // Helper method to check if a character is a vowel
    public static boolean isVowel(char ch) {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
               ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U';
    }
}
