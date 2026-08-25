class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        result = ""
        for ch in s :
            freq[ch] = freq.get(ch,0)+1

        chars = sorted(freq, key=freq.get, reverse=True)

        for ch in chars:
            result +=ch*freq[ch]

        return result



        
       
        
            

        
        