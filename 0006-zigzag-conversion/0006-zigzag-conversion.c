char* convert(char* s, int numRows) {
    if (numRows == 1 || strlen(s) <= numRows) {
        return s;
    }

    int len = strlen(s);
    char** rows = (char**)malloc(numRows * sizeof(char*));
    for (int i = 0; i < numRows; i++) {
        rows[i] = (char*)malloc((len + 1) * sizeof(char)); // Allocate max possible length
        rows[i][0] = '\0'; // Initialize each row
    }

    int curRow = 0;
    int movingDown = 1; // 1 for moving down, 0 for moving up

    for (int i = 0; i < len; i++) {
        int rowIndex = curRow;
        int charIndex = strlen(rows[rowIndex]);
        rows[rowIndex][charIndex] = s[i];
        rows[rowIndex][charIndex + 1] = '\0'; // Null-terminate the string

        if (curRow == 0) {
            movingDown = 1; // Move down if at the top row
        } else if (curRow == numRows - 1) {
            movingDown = 0; // Move up if at the bottom row
        }

        curRow += movingDown ? 1 : -1; // Move the current row pointer based on the direction
    }

    // Combine all rows into the final result
    char* result = (char*)malloc((len + 1) * sizeof(char));
    result[0] = '\0';
    for (int i = 0; i < numRows; i++) {
        strcat(result, rows[i]);
        free(rows[i]); // Free the memory allocated for each row
    }
    free(rows); // Free the memory allocated for row pointers

    return result;
}
    
