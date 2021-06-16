class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_map = dict()
        for i, val in enumerate(nums):
            diff = target - val
            if diff not in val_map:
                val_map[val] = i
            else:
                return [val_map.get(diff), i]
            
        