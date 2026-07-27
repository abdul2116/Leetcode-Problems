from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0 
        @cache
        def solve(index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            
            ways = solve(index+1)

            if index+1 < len(s):
                two_digit_value = int(s[index:index+2])
                if 10 <= two_digit_value <= 26:
                    ways += solve(index+2)
            return ways
        return solve(0)