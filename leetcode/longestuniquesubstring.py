# runtime complexity: O(n)
# space complexity: O(n) for the additional dictionary data structure
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # size of the string
        n = len(s)
        # the longest substring
        max_len = 0
        
        # auxilliary data structure for storing character counts
        mp = {}
        i = 0
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
                
            max_len = max(max_len, j - i + 1)
            mp[s[j]] = j + 1
            
        return max_len
        
        
        
        