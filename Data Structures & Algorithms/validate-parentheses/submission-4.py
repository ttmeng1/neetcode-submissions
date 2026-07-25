class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {"(":")",
                "{":"}",
                "[":"]"}
        for char in s:
            if char in map:
                stack.append(char)
            else:
                if stack == []:
                    return False
                elif char != map[stack[-1]]:
                    return False
                else:
                    stack.pop()
        return stack == []
        