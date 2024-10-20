class Solution {
    public String reverseWords(String s) {
        // Split the input string by one or more spaces (using "\\s+" as regex)
        // This also trims the leading and trailing spaces
        String[] words = s.trim().split("\\s+");

        // Use a StringBuilder to reverse the words
        StringBuilder sb = new StringBuilder();

        // Append words in reverse order
        for (int i = words.length - 1; i >= 0; i--) {
            sb.append(words[i]);
            if (i > 0) { // Only add space if not the last word
                sb.append(" ");
            }
        }

        // Return the reversed string
        return sb.toString();
    }
}
