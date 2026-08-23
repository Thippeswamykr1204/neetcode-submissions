class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(i.lower() for i in s if i.isalnum())

        return t == t [::-1]