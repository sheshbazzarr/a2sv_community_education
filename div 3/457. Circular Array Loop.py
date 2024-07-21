class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for start in range(n):
            fast, slow = start, start
            ispos = True if nums[fast] > 0 else False
            while True:
                # fast runs 2 time
                if fast == (fast + nums[fast]) % n:
                    # self loop
                    break
                fast = (fast + nums[fast]) % n
                cond = True if nums[fast] > 0 else False # check if the nums[seq[j]] is all pos or neg
                if ispos != cond:
                    break

                if fast == (fast + nums[fast]) % n:
                    # self loop
                    break
                fast = (fast + nums[fast]) % n
                cond = True if nums[fast] > 0 else False
                if ispos != cond:
                    break
                
                # slow runs just 1 time
                # no need to check for self loop, since fast pointer already checked
                slow = (slow + nums[slow]) % n

                if fast == slow:
                    return True
        return False
