from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0 
        max_len = 0
        for i in range(len(nums)):
            freq[nums[i]] += 1
            while freq[nums[i]] > k :
                freq[nums[left]] -= 1
                left += 1
            max_len = max(max_len,i-left+1)
        return max_len        