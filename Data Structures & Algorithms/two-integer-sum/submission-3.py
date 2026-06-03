class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mpp:
                return [mpp[diff], i]
            mpp[n] = i