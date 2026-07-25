class Solution:
    def maxProduct(self, n: int) -> int:
        dig = [int(digit) for digit in str(n)]
        dig.sort(reverse=True)
        return dig[0] * dig[1]
        
