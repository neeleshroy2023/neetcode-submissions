class Solution:
    def isPalindrome(self, s: str) -> bool:
        a_text = "".join(char for char in s.lower() if char.isalnum())
        left = 0
        right = len(a_text) - 1
        while left < right:
            if a_text[left] != a_text[right]:
                return False
            left += 1
            right -= 1
        return True
        