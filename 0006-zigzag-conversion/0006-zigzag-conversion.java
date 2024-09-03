class Solution {
    public String convert(String s, int numRows) {
        if(numRows==1 || s.length()<=numRows){
            return s;
        }
        StringBuilder [] rows = new StringBuilder[numRows];
        for (int i =0;i<numRows;i++){
            rows[i] = new StringBuilder();
        }
        int curRow = 0;
        boolean movingDown = true;

        for (char ch :s.toCharArray()){
            rows[curRow].append(ch);
            if(curRow ==0){
                movingDown = true;
            }
            else if (curRow ==numRows-1){
                movingDown = false;
            }

            if(movingDown){
                curRow++;
            }
            else{
                curRow--;
            }

        }
           // Combine all the rows to form the final converted string
        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) {
            result.append(row);
        }

        return result.toString();
    }
    }
