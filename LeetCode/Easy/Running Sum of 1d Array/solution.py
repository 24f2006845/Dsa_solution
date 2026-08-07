class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumArr = []
        sumArr.append(nums[0])
        for i in range(1,len(nums)):
            elem = sumArr[i-1]+nums[i]
            sumArr.append(elem)
        return sumArr
            

