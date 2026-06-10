class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False
        mpp1 = {}
        mpp2 = {}
        for ch in s:
            if ch in mpp1:
                mpp1[ch] += 1
            else:
                mpp1[ch] = 1
        for ch in t:
            if ch in mpp2:
                mpp2[ch] += 1
            else:
                mpp2[ch] = 1
        
        for k in mpp1:
            if k in mpp2 and mpp2[k] == mpp1[k]:
                continue
            return False
        return True