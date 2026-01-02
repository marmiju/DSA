class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # converted each into string 
        s = "".join(map(str,digits))
        
        nums = int(s) + 1
        return [int(x) for x in str(nums)]
        