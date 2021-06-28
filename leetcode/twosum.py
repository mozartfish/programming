# runtime complexity: O(n) where n represents the number of numbers
# space complexity: O(n) - dictionary used for storing values
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary to store values in the list 
        num_map = dict()
        for i, value in enumerate(nums):
            # get the difference
            diff = target - value
            
            # check if the value is in the map 
            if diff in num_map:
                return [num_map.get(diff), i]
            else:
                num_map[value] = i