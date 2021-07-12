# runtime complexity: O(n) where n represents all the integers in nums
# spacetime complexity: O(n) for the set because we add n elements to the set in the worst case
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        1. keep track of frequency - dictionary
        '''
        
        fre = Counter(nums)
        
        for key in fre:
            if fre[key] >= 2:
                return True
        
        return False