class Solution:
    def isPalindrome(self, x: int) -> bool:
        min_o = -2**31
        max_o = 2**31 - 1
        
        if x not in range(min_o, max_o) or x < 0:
            return False
        
        result = int(str(x)[::-1])
        
        if result not in range(min_o, max_o):
            return False
        
        if result != x:
            return False
        
        return True
        