# runtime complexity: O(n) - where n represents the number of characters in the string
# spacetime complexity: O(n) - created a stack to store the items in the string s
class Solution:
    def isValid(self, s: str) -> bool:
        p_stack = []
        p_map = {")": "(", "}": "{", "]" : "["}
        
        for char in s:
            if char in p_map:
                top = p_stack.pop() if p_stack else '#'
                if p_map[char] != top:
                    return False
            else:
                p_stack.append(char)
            
        return not p_stack
                