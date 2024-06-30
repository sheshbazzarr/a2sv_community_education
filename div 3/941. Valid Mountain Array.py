class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # two person
        A=0   # one end 
        B=len(arr)-1 # the other side
        D=len(arr) # distance between them 
        while A+1<D and arr[A]<arr[A+1]: # first person climb the mountain 
            A+=1 
        while B>0 and arr[B]<arr[B-1]: # second person climb the mountain 
            B-=1
        return 0<A==B<D-1 # if Person A and B Both move and meet at the pick of mountain 
    
    
    # inspired by lee215
