class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean += ch.lower()
        j = len(clean)-1
        for i in range(len(clean)):
            if clean[i] != clean[j]:
                return False
            j-=1
        return True

        