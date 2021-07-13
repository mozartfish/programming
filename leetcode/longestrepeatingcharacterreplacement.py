# runtime complexity: O(n)
# space time complexity: O(n) for the dictionary data structure
# trick: sliding window with additional data structure

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        1. keep track of character counts
        2. sliding window to keep track of the longest length
        3. keep track of maximum substring
        '''
        
        count = {}
        l = 0
        res = 0
        maxf = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
        