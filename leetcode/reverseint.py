    def reverse(self, x: int) -> int:
        result = 0
        if x > 0:
            result = int(str(x)[::-1])
        if x < 0:
            result = -1 * int(str(x * -1)[::-1])
        
        # overflow
        min_o = -2**31
        max_o = 2**31 - 1
        
        if result not in range(min_o, max_o):
            return 0
        else:
            return result