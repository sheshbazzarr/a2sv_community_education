class Solution:
    def countSegments(self, s: str) -> int:
        # Trim leading and trailing spaces
        s = s.strip()
        # If the string is empty, return 0
        if not s:
            return 0
        # Split the string into segments based on spaces
        segments = s.split()
        # Return the number of segments
        return len(segments)