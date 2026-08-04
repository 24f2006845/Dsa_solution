class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_length = 0
        if len(nums) ==0 :
            return 0
        for num in s:
            if num-1 not in s:
                current = num
                length = 1
                while current+1 in s:
                    current+=1
                    length +=1
                max_length = max(max_length, length)
        return max_length
