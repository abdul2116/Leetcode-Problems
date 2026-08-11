class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        current_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                current_sum += nums[i]
            else:
                break
        nums_set = set(nums)
        ans = current_sum
        while ans in nums_set:
            ans+=1
        return ans
        