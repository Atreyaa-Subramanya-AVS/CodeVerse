from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
    

nums = [1,1,2,3,3,4,4,8,8]

print(Solution().singleNonDuplicate(nums))