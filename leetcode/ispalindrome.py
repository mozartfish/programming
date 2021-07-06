# tricK: push pop method
# runtime complexity: O(N) where n represents the number of digits
# space complexity: O(1) since no additional data structures are used

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        def divide(number, divider):
            return int(number * 1.0 / divider)
        
        def mod(number, m):
            return number % m
        
        copy = x
        res = 0
        
        while x:
            pop = mod(x, 10)
            x = divide(x, 10)
            res = res * 10 + pop
            
        return copy == res