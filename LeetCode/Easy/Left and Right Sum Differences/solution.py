class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            suffix[j] = suffix[j+1]+nums[j+1] 
        for k in range(len(nums)):
            answer[k] = abs(prefix[k]-suffix[k])
        print(prefix)
        print(suffix)
        return answer

        