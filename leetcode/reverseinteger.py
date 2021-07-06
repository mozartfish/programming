# trick: push pop method
# runtime: O(n) for all the digits in the number
# space complexity: O(1) because no additional data structures needed
class Solution:
    def reverse(self, x: int) -> int:
        def divide(number, divider):
            return int(number * 1.0 / divider)
        
        def mod(number, m):
            if number < 0:
                return number % -m
            else:
                return number % m
        
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        
        res = 0
        while x:
            pop = mod(x, 10)
            x = divide(x, 10)
            res = res * 10 + pop
        
        if res < MIN_INT or res > MAX_INT:
            return 0
        
        return res
        '''
        123 
        
        1. 123 % 10 = 3
        2. 13 / 10 = 12
        3. 12 % 10 = 2
        4. 12 / 10 = 1
        5. 1 % 10 = 1
        6. 1 / 10 = 0
        '''
        
# brute force solution
# runtime: O(n) to reverse all the characters in the list
# space complexity: O(n) for the number of digits in the number
class Solution:
    def reverse(self, x: int) -> int:
        '''
        1. range is -2^31 to 2^31 - 1
        2. convert integer to positive value 
        3. convert integer into a list of characters and revese
        4. convert string to integer
        5. check if the integer is within the range 
        6. return the result 
        '''
        
        rev = x
        if x < 0:
            rev = -1 * x
        
        rev = str(rev)
        
        rev = rev[::-1]
        rev = int(rev)
        
        if rev in range(-2**31, 2**31 - 1):
            if x < 0:
                return -1 * rev
            return rev
        else:
            return 0
            
            