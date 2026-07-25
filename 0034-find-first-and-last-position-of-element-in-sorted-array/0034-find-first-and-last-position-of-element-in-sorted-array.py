class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_boundary(find_left):
            low, high = 0 , len(nums)-1
            boundary = -1
            while low<=high:
                mid = (low+high)//2
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    boundary = mid
                    if find_left:
                        high = mid - 1
                    else:
                        low = mid + 1
            return boundary
        return [find_boundary(True), find_boundary(False)]