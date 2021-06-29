# runtime complexity: O(n + m) because we have to merge two lists of different lengths
# spacetime complexity: O(n + m) for the additional array we use for merging and finding the median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = [0] * (len(nums1) + len(nums2))
        
        # merge data
        i = j = k = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr[k] = nums1[i]
                i += 1
            else:
                arr[k] = nums2[j]
                j += 1
            
            k += 1
            
        # check for any elements left
        while i < len(nums1):
            arr[k] = nums1[i]
            i += 1
            k += 1
        while j < len(nums2):
            arr[k] = nums2[j]
            j += 1
            k += 1
        
        # find the median
        if len(arr) % 2 == 0:
            mid_index = len(arr) // 2
            prev = mid_index - 1
            
            result = (arr[mid_index] + arr[prev]) / 2
            return result
        else:
            mid_index = len(arr) // 2
            return arr[mid_index]