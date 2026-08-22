class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        max_rotation = len(s)
        i = 0
        while s!=goal:
            if i > max_rotation:
                return False
            s = s[1:] + s[0]
            i+=1
            if s == goal:
                break
        return True


        