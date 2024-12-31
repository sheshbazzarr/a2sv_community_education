#include <vector>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        // Create a 2D DP table with dimensions m x n
        vector<vector<int>> dp(m, vector<int>(n, 1));  // Initialize first row and first column to 1
        
        // Fill the DP table
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];  // Sum of ways from above and left
            }
        }
        
        return dp[m - 1][n - 1];  // The bottom-right corner contains the result
    }
};
