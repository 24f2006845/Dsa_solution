class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i],0)+1
        if len(s) != len(t):
            return False
        for k in range(len(t)):
            if t[k] in freq:
                if freq[t[k]] >0:
                    freq[t[k]]-=1
                else:
                    return False
            else:
                return False
        return True
        