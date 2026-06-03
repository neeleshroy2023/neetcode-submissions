class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mpp = {}
        for c in s:
            if c in mpp:
                mpp[c] += 1
            else:
                mpp[c] = 1
        
        for c in t:
            if c in mpp:
                if mpp[c] > 1:
                    mpp[c] -= 1
                else:
                    del mpp[c]
            else:
                return False
        return True
        