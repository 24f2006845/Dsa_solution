class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = [1] * len(nums)
        suffix = [1]* len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            suffix[j] = suffix[j+1] * nums[j+1]
        for i in range(len(nums)):
            answer[i] = prefix[i] * suffix[i]
        print(prefix)
        print(suffix)
        print(answer)

        return answer


        