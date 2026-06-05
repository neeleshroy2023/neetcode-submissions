class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        f1 = {}
        f2 = {}

        for ch in s:
            if ch in f1:
                f1[ch] += 1
            else:
                f1[ch] = 1
        
        for ch in t:
            if ch in f2:
                f2[ch] += 1
            else:
                f2[ch] = 1

        for (i, j) in f1.items():
            if i not in f2:
                return False
            if f2[i] != j:
                return False
        return True