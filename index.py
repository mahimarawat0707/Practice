class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        
        while i < n - 1:   # stop before last bit
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        
        # If we end exactly at the last index, it's a 1-bit character
        return i == n - 1
