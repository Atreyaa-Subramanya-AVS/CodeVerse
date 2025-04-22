from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Sorts the array so that all 0s come first, then 1s, then 2s.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

if __name__ == "__main__":
    solution = Solution()

    nums1 = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums1)
    print(f"Input: nums = [2, 0, 2, 1, 1, 0], Output: nums = {nums1}")