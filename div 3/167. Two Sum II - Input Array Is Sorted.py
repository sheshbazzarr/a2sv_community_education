class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        low, high = 0, n - 1

        while low < high:
            cur_sum = numbers[low] + numbers[high]
            if cur_sum < target:
                low += 1
            elif cur_sum > target:
                high -= 1
            else:
                return [low + 1, high + 1]

        return [low + 1, high + 1]
