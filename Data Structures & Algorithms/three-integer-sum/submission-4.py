class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        anchor = 0
        n = len(nums)
        triplets = []
        while anchor < n - 2:
            left = anchor + 1
            right = n - 1
            while left < right:
                s = nums[anchor] + nums[left] + nums[right]
                if s == 0:
                    triplets.append([nums[anchor], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1
            anchor += 1
            while anchor < n - 2 and nums[anchor] == nums[anchor - 1]:
                anchor += 1
        return triplets

