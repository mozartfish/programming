# runtime complexity: O(n) since we iterate over each integer in the roman integer
# space time complexity: O(1) since we have a fixed data structure for storing basic roman numerals

class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        1. map integers to roman values 
        2. loop through values to calculate the correct number and add to a running sum
        3. return value
        '''
        
        # mapping values
        sym_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        total = sym_map.get(s[-1])
        for i in reversed(range(len(s) - 1)):
            if sym_map.get(s[i]) < sym_map.get(s[i + 1]):
                total -= sym_map.get(s[i])
            else:
                total += sym_map.get(s[i])
        
        return total
            
            
            