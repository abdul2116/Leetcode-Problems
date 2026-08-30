class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        min_index = nums.index(min_val)
        max_index = nums.index(max_val)
        i = min(min_index,max_index)
        j = max(min_index,max_index)
        
        cost = min(
            j+1,
            len(nums)-i,
            (i+1) + (len(nums)-j)
        )
        return cost
