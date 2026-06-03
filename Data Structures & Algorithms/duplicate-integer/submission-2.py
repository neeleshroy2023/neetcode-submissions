class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mpp = {}
        for i, n in enumerate(nums):
            if n in mpp and abs(mpp[n] - i):
                return True
            else:
                mpp[n] = i
        return False
        