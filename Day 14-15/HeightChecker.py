from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for h1, h2 in zip(heights, expected):
            if h1 != h2:
                count += 1
        return count

sol = Solution()
print(sol.heightChecker([1, 1, 4, 2, 1, 3]))
