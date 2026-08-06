class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        canidate = n

        while True:
            product = 1
            temp = canidate
            while temp>0:
                digit = temp%10
                product *= digit
                temp = temp//10
                if product %t ==0:
                    return canidate
            canidate +=1
        