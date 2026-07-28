class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        sorted_left = sorted(s[:n//2])

        mid = [s[n//2]] if n%2 != 0 else []

        return "".join(sorted_left + mid + sorted_left[::-1])