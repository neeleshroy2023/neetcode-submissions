class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for item in strs:
            encoded += str(len(item)) + "#" + item
        return encoded

    def decode(self, s: str) -> List[str]:
        i=0
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])

            start = j + 1
            end = start + length
            result.append(s[start:end])
            i = end
        return result

