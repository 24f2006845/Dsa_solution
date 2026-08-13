class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total+=nums[i]
        left = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] -left
            if left==rightSum:
                return i
            left+=nums[i]
        return -1
            
            

            

           

         