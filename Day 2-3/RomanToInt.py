class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]

        return total

if __name__ == "__main__":
    solution = Solution()

    roman1 = "III"
    result1 = solution.romanToInt(roman1)
    print(f"Input: s = '{roman1}', Output: {result1}")