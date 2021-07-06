# runtime complexity: O(n) where n represents the number of numbers
# space complexity: O(n) - dictionary used for storing values
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        1. calculate the difference between the target value and each value in the list
        2. check if difference is in the list
        3. return the indexes of the two values whose sum equals the target value 
        '''
        
        # data structure for storing difference and index
        num_dict = {}
        
        for index, value in enumerate(nums):
            diff = target - value
            if diff not in num_dict:
                num_dict[value] = index
            else:
                return [num_dict.get(diff), index]
  
                
            