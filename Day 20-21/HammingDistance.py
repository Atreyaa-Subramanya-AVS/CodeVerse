class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            distance += xor & 1
            xor >>= 1
        return distance

sol = Solution()
print(sol.hammingDistance(1, 4))
print(sol.hammingDistance(3, 1))
