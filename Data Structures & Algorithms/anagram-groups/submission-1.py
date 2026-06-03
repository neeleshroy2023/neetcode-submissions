class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {}
        for word in strs:
            freq = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                freq[idx] += 1
            hash_id = ''.join([f'#{f}' for f in freq])
            
            if hash_id in mpp:
                mpp[hash_id].append(word)
            else:
                mpp[hash_id] = [word]
        anagrams = []
        for an in mpp:
            anagrams.append(mpp[an])
        return anagrams