class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)

        count = {}

        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in count:
                count[sorted_nums[i]] = i

        result = []

        for num in nums:
            result.append(count[num])

        return result