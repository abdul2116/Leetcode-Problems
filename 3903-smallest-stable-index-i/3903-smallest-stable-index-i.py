class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            big = max(nums[0:i+1])
            small = min(nums[i:])

            if big - small <= k:
                return i
        return -1
