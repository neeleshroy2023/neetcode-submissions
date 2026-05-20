class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # [1,2,6,36]
        # [48,48,24,6]
        n = len(nums)
        prefix = [1 for _ in range(0, n)]
        suffix = [1 for _ in range(0, n)]
        prefix[0] = nums[0]
        suffix[n-1] = nums[n-1]
        result = [1 for _ in range(0, n)]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        for i in range(0, n):
            if i - 1 == -1:
                result[i] = suffix[i+1]
            elif i + 1 == n:
                result[i] = prefix[i-1]
            else:
                result[i] = prefix[i-1] * suffix[i+1]
        return result