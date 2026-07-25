class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[zero] = nums[i]
                zero+=1
            else:
                continue
        for i in range(zero,len(nums)):
            nums[i] = 0
        return nums
        