import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(char.lower() for char in s if char.isalnum())
        if res == res[::-1]:
            return True
        return False