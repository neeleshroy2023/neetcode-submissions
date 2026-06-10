class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {}
        results = []
        for word in strs:
            freq_map = [0] * 26
            for ch in word:
                index = ord(ch) - ord('a')
                freq_map[index] += 1
            mpp_index = '#'.join([str(c) for c in freq_map])
            if mpp_index in mpp:
                mpp[mpp_index].append(word)
            else:
                mpp[mpp_index] = [word]

        for i in mpp:
            results.append(mpp[i])
        return results