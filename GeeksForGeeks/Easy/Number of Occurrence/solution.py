class Solution:
    def countFreq(self, arr, target):
        # code here
        start = -1
        end = -1
        low = 0
        high = len(arr)-1
        while low <=high:
            mid = (low+high)//2
            if arr[mid]<target:
                low= mid+1
            elif arr[mid]> target:
                high = mid -1
            else:
                start = mid 
                high = mid -1
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = (low+high)//2
            if arr[mid]< target:
                low = mid+1
            elif arr[mid]>target:
                high = mid-1
            else:
                end = mid
                low = mid+1
        freq = end-start+1
        if start == -1:
            return 0
        else:
            return freq