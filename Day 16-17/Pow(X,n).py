class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x: float, n: int) -> float:
            if n == 0:
                return 1
            half = helper(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            x = 1 / x
            n = -n

        return helper(x, n)
    
sol = Solution()
print(sol.myPow(2.00000, 10))
print(sol.myPow(2.10000, 3))
print(sol.myPow(2.00000, -2))
