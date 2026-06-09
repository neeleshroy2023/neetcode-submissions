class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                prev_idx, prev_val = stack.pop()
                res[prev_idx] = idx - prev_idx
            stack.append((idx, val))
        return res