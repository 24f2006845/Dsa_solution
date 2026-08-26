class Solution:
    def romanToInt(self, s: str) -> int:
        current = 0
        previous = 0
        total = 0
        roman = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }

        for i in range(len(s)-1,-1,-1):
            value = roman[s[i]]
            current = value 
            if current < previous:
                total -= current
                previous = current
            else:
                total +=current
                previous = current
        return total



        