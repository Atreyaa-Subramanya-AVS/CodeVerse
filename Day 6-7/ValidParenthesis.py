class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in close_map:
                top = stack.pop() if stack else '#'
                if close_map[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack


if __name__ == "__main__":
    solution = Solution()

    s1 = "(){}[]"
    print(f"{s1} is {"valid" if solution.isValid(s1) else "not valid"} parenthesis.")

    s2 = "(]"
    print(f"{s2} is {"valid" if solution.isValid(s2) else "not a valid"} parenthesis.")