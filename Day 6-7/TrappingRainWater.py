from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        trapped = 0

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                mid = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                depth = min(height[left], h) - height[mid]
                trapped += width * depth

            stack.append(i)

        return trapped

if __name__ == "__main__":
    solution = Solution()
    
    test_height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"Trapped water: {solution.trap(test_height)}")
