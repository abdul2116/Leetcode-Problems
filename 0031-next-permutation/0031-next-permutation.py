class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = -1
        n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                idx = i
                break
        if idx != -1:
            for j in range(n-1,idx,-1):
                if nums[j] > nums[idx]:
                    nums[idx],nums[j] = nums[j], nums[idx]
                    break
        left = idx+1
        right = n-1
        while left < right:
            nums[left] , nums[right] = nums[right] , nums[left]
            left += 1
            right -= 1 
        return nums