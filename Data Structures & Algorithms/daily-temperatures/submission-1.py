class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for today_index, today_temp in enumerate(temperatures):
            while stack and today_temp > stack[-1][0]:
                prev_temp, prev_index = stack.pop()
                res[prev_index] = today_index - prev_index
            stack.append((today_temp, today_index))
        return res