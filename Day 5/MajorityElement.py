from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

if __name__ == "__main__":
    solution = Solution()

    nums1 = [3, 2, 3]
    result1 = solution.majorityElement(nums1)
    print(f"Input: nums = {nums1}, Output: {result1}")