class Solution:
    def isValid(self, s: str) -> bool:
        mpp = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }

        stack = []

        for c in s:
            if c in mpp.keys():
                stack.append(mpp[c])
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != c:
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        return False