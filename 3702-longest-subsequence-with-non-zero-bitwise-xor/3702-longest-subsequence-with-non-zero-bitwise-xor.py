class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if all(x==0 for x in nums):
            return 0
        xor = 0
        for i in nums:
            xor ^= i
        if xor!=0:
            return n
        else:
            return n-1

            

    
            

        