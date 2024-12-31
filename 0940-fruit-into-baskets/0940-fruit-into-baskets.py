

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        fruit_counts = defaultdict(int)
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            fruit_counts[fruits[right]] += 1

            # If more than two types of fruits are in the window, shrink the window
            while len(fruit_counts) > 2:
                fruit_counts[fruits[left]] -= 1
                if fruit_counts[fruits[left]] == 0:
                    del fruit_counts[fruits[left]]
                left += 1

            # Update the maximum number of fruits
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits