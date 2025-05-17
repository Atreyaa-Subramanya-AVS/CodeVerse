class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return self.isPositive(n) and self.isPowerOfTwo(n) and self.isPowerOfFourPosition(n)

    def isPositive(self, n: int) -> bool:
        return n > 0

    def isPowerOfTwo(self, n: int) -> bool:
        return (n & (n - 1)) == 0

    def isPowerOfFourPosition(self, n: int) -> bool:
        return (n - 1) % 3 == 0

sol = Solution()
print(sol.isPowerOfFour(16))
print(sol.isPowerOfFour(8))
print(sol.isPowerOfFour(1))
print(sol.isPowerOfFour(0))
