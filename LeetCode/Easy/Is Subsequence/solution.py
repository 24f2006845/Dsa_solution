class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        right = 0
        if len(s)==0 and len(t) ==0:
            return True

        while right < len(t):
            if left < len(s) and s[left] == t[right]:
                left += 1

            right += 1

            if left == len(s):
                return True

        return False    