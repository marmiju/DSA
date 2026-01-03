class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base case
        dpA = 6  # ABC
        dpB = 6  # ABA
        
        for _ in range(2, n + 1):
            newA = (dpA * 2 + dpB * 2) % MOD
            newB = (dpA * 2 + dpB * 3) % MOD
            dpA, dpB = newA, newB
        
        return (dpA + dpB) % MOD
