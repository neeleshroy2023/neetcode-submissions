class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        frequency_map = {}
        topk = []
        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 1
            else:
                frequency_map[num] += 1
        buckets = [[] for _ in range(0, n+1)]
        for key in frequency_map:
            buckets[frequency_map[key]].append(key)
        print(buckets)

        for i in range(n, 0, -1):
            if len(buckets[i]) > 0:
                for item in buckets[i]:
                    if k > 0:
                        topk.append(item)
                        k-=1
                    else:
                        return topk
        return topk
        

        