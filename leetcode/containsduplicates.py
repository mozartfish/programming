# runtime complexity: O(n) where n represents all the integers in nums
# spacetime complexity: O(n) for the set because we add n elements to the set in the worst case
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = False
        num_set = set()
        
        for i, value in enumerate(nums):
            if nums[i] not in num_set:
                num_set.add(nums[i])
            else:
                result = True
        
        return result
        