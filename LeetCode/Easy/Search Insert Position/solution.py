class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low =0
        value = len(nums)
        high = len(nums)-1
        while low <=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid-1
                value = mid
            else:
                low= mid+1
        return value
        