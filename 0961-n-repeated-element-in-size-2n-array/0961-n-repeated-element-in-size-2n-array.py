class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2

        nums_count = Counter(nums)

        for num, freq in nums_count.items():
            if freq == n :
                return num

        