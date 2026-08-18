from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        
        count = Counter(nums)

        if k == 1:
            return max([num for num in nums if count[num]==1],default =-1)
        
        # to check for 1<k<n

        candidates = []

        if count[nums[0]] == 1:
            candidates.append(nums[0])
        if count[nums[-1]] == 1:
            candidates.append(nums[-1])
        
        return max(candidates,default=-1)