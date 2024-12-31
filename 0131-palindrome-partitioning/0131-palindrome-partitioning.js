/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    const result = [];

    // Helper function to check if a string is a palindrome
    const isPalindrome = (str) => {
        let left = 0;
        let right = str.length - 1;
        while (left < right) {
            if (str[left] !== str[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    };

    // Backtracking function to find all palindrome partitions
    const backtrack = (start, currentPartition) => {
        if (start === s.length) {
            result.push([...currentPartition]); // When we reach the end, add the current partition
            return;
        }

        // Try every possible substring starting from 'start'
        for (let end = start + 1; end <= s.length; end++) {
            const substring = s.slice(start, end);
            if (isPalindrome(substring)) {
                currentPartition.push(substring);  // Add palindrome substring to the partition
                backtrack(end, currentPartition);  // Recurse for the remaining part of the string
                currentPartition.pop();  // Backtrack by removing the last added substring
            }
        }
    };

    // Start the backtracking from index 0 with an empty partition
    backtrack(0, []);
    
    return result;
};
