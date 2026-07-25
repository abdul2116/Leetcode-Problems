class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        final = [0] * len(nums)
        pos_idx = 0
        neg_idx = 1
        for num in nums:
            if num > 0:
                final[pos_idx] = num
                pos_idx += 2
            else:
                final[neg_idx] = num
                neg_idx += 2
        return final 
        
            
        