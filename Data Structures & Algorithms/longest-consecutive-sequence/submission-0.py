class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for i in nums:
            if i-1 not in s:
                length = 1
                while i + length in s:
                    length += 1
                best = max(length, best)
        return best
        