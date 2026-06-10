class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp = {}
        freq = [[] for num in range(len(nums) + 1)]
        res = []
        for num in nums:
            if num in mpp:
                mpp[num] += 1
            else:
                mpp[num] = 1
        for idx in mpp:
            freq[mpp[idx]].append(idx)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                k-=1
                if k == 0:
                    return res
        return res