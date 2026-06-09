class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for today_idx, today_temp in enumerate(temperatures):
            while stack and today_temp > stack[-1][0]:
                prev_temp, prev_idx = stack.pop()
                res[prev_idx] = today_idx - prev_idx
            
            stack.append((today_temp, today_idx))
        return res

        