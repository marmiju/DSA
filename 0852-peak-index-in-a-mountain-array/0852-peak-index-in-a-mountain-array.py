class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n = len(arr)
        st = 0
        end = n-1

        while st<end:
            mid = st + (end-st)//2
            if arr[mid]<arr[mid+1]:
                st = mid+1
            else:
                end = mid

        return st
        