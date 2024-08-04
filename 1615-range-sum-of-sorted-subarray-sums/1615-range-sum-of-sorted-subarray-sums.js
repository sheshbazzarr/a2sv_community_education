/**
 * @param {number[]} nums
 * @param {number} n
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var rangeSum = function(nums, n, left, right) {
    const list=[]
    for (let i =0;i<n;i++){
        let sum = 0
        for (let j=i;j<n;j++){
            sum+=nums[j]
            list.push(sum)
        }
    }
    list.sort((a,b)=>a-b)
    const mod =10**9+7
    return list.slice(left-1,right)
        .reduce((prev,curr)=>(prev+curr) %mod,0)
};