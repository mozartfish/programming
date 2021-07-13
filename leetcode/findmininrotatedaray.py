# runtime complexity: O(log n)
# spacetime complexity: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if length is 1
        if len(nums) == 1:
            return nums[0]
        
        # pointers
        left = 0
        right = len(nums) - 1
        
        # if the list is still in ascending order
        if nums[right] > nums[0]:
            return nums[0]
        
        # binary search
        while right >= left:
            
            # calculate mid point
            mid = left + (right - left) // 2
            
            # if middle number is greater than the next number
            # we found the min
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            # if the previous number is greater than the mid
            # then we know that the mid is the min
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            # search the right half of the array
            if nums[mid] > nums[0]:
                left = mid + 1
                
            # search the left half of the array
            else:
                right = mid - 1