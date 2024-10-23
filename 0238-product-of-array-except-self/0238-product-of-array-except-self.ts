function productExceptSelf(nums: number[]): number[] {
    let n = nums.length;
    const result = new Array(n);
    // Calculate prefix products
    let prefixProduct = 1;
    for (let i =0;i<n;i++){
        result[i]=prefixProduct;
        prefixProduct *=nums[i];

    }
    // Calculate suffix products and finalize the result 
    let suffixProduct =1;
    for (let i=n-1;i>=0;i--){
        result[i]*=suffixProduct;
        suffixProduct *=nums[i];
    }
    return result;
};