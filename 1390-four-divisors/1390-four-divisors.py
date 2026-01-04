class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0

        for n in nums:
            divisors = set([1,n])
            for i in range(2,int (n**0.5) + 1):
                if n%i==0:
                    divisors.add(i)
                    divisors.add(n//i)
            
                if len(divisors) > 4:
                    break

            if len(divisors) == 4:
                total_sum += sum(divisors)
        
        return total_sum
    
        