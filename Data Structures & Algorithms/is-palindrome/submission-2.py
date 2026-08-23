class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(i.lower() for i in s if i.isalnum())

        left = 0
        right = len(t)-1
        while left < right:
            if t[left] != t[right]:
                return False
            else:
                left += 1
                right -= 1
        return True