class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")

        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)

if __name__ == "__main__":
    solution = Solution()

    s1 = "/home/user/Documents/../Pictures"

    print(f"Simplified Path: {solution.simplifyPath(s1)}")