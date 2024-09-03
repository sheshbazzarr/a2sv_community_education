function convert(s: string, numRows: number): string {
    if(numRows ===1 || s.length <= numRows){
        return s;
    }
    const rows: string[] = new Array(numRows).fill('');
    let curRow = 0;
    let movingDown = true;

    for (const char of s){
        rows[curRow]+=char
        if(curRow === 0){
            movingDown = true;
        }
        else if (curRow ===numRows-1){
            movingDown = false;
        }
        if(movingDown){
            curRow+=1;
        }
        else{
            curRow-=1;
        }
    }
    return rows.join('');
    
};