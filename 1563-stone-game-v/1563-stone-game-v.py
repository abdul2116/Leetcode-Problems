from functools import lru_cache
import sys

sys.setrecursionlimit(2000)

class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        def get_sum(i, j):
            return prefix[j + 1] - prefix[i]

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0
            
            max_score = 0
            for p in range(i, j):
                left_sum = get_sum(i, p)
                right_sum = get_sum(p + 1, j)
                
                if left_sum < right_sum:
                    # Pruning: if our current max_score is already better than or equal 
                    # to what we could possibly achieve with left_sum + max future score, skip
                    if max_score >= left_sum * 2:
                        continue
                    max_score = max(max_score, left_sum + dp(i, p))
                    
                elif left_sum > right_sum:
                    # Pruning: as p increases, left_sum increases and right_sum decreases.
                    # If max_score is already higher than right_sum * 2, further splits will only make it worse.
                    if max_score >= right_sum * 2:
                        break
                    max_score = max(max_score, right_sum + dp(p + 1, j))
                    
                else:
                    max_score = max(max_score, left_sum + dp(i, p), right_sum + dp(p + 1, j))
                    
            return max_score

        return dp(0, n - 1)