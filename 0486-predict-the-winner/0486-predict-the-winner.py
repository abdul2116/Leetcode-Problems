class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}

        def helper(left: int, right: int) -> int:
            # Base case: only one number left
            if left == right:
                return nums[left]
            
            # Check memoization table
            if (left, right) in memo:
                return memo[(left, right)]
            
            # Choice 1: Pick the left number
            pick_left = nums[left] - helper(left + 1, right)
            
            # Choice 2: Pick the right number
            pick_right = nums[right] - helper(left, right - 1)
            
            # Store and return the max advantage
            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]

        # If Player 1's net score difference is >= 0, they win or tie
        return helper(0, len(nums) - 1) >= 0