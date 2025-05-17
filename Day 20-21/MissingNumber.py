from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n + 1):
            res ^= i
        for num in nums:
            res ^= num
        return res

sol = Solution()
print(sol.missingNumber([3, 0, 1]))
print(sol.missingNumber([0, 1]))