from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        
        freq = Counter(word)
        sorted_freq = sorted(freq.values(),reverse=True)

        total_pushes = 0
        
        for i,count in enumerate(sorted_freq):
            pushes_per_key = (i//8)+1
            total_pushes += count * pushes_per_key
        
        return total_pushes