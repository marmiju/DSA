class Solution:
    def search(self, nums: list[int], tar: int) -> int:
        n = len(nums)

        st =0
        end = n-1

        while st<=end:
            mid = st + (end-st)//2
            if nums[mid] == tar:
                return mid
            
            if nums[st] <= nums[mid]: #left side sorted
                if nums[st]<=tar and nums[mid]>=tar:
                    end = mid -1
                else:
                    st = mid +1
            else: # right side sorted 
                if nums[mid]<= tar and nums[end]>=tar:
                    st = mid +1 
                else:
                    end = mid -1
        return -1

        

            
        