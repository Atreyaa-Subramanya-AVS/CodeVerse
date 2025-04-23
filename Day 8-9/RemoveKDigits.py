from collections import deque

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1
            
        result = ''.join(stack).lstrip('0')

        return result if result else '0'
    
if __name__ == "__main__":
    solution = Solution()

    num1 = "1432219"
    k1 = 3

    print(f"Smallest Digit after removing {k1} digits from {num1} is: {solution.removeKdigits(num1,k1)}")