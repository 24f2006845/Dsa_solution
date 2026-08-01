class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for val in words:
            if val.startswith(pref):
                count+=1
        return count

        