# runtime complexity: O(s + t) because counter is a dictionary and may possibly use a for loop
# under the hood to insert items

# space complexity: O(s + t) because two dictionaries of various size were created
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = Counter(s)
        t_map = Counter(t)
        
        if s_map != t_map:
            return False
        
        return True