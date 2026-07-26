class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {"(":")",
                "{":"}",
                "[":"]"}
        for c in s:
            if c in map:
                stack.append(c)
            else:
                if stack != [] and c == map[stack[-1]]:
                    stack.pop(-1)
                else:
                    return False
        return stack == []
        