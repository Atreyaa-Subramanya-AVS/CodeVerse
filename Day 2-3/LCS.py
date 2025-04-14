from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        long_streak = 0
        for num in sett:
            if num - 1 not in sett:
                current_num = num
                current_streak = 1

                while current_num + 1 in sett:
                    current_num += 1
                    current_streak += 1
                long_streak = max(long_streak, current_streak)

        return long_streak

if __name__ == "__main__":
    solution = Solution()

    nums1 = [100, 4, 200, 1, 3, 2]
    result1 = solution.longestConsecutive(nums1)
    print(f"Input: nums = {nums1}, Output: {result1}")