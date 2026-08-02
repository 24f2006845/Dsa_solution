class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons = 0
        count = 0 
        for val in nums:
            if val ==1:
                count = count + 1
                print(count)
                if count > max_cons:
                    max_cons = count
                print(max_cons)
            else:
                count -= count
                

        return max_cons

        