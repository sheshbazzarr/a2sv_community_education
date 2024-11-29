class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1_next_map={n:i for i,n in enumerate(nums1)}
        result=[-1]*len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in nums1_next_map:
                continue
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    inde=nums1_next_map[nums2[i]]
                    result[inde]=nums2[j]
                    break
        return result