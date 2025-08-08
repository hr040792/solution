def plusOne(self, digits: List[int]) -> List[int]:
    
    for i in range (len(digits) - 1, -1, -1): # iterate from the last digit to the first

        # if the current digit is less than 9 then add 1
        if digits[i] < 9:
            digits[i] += 1
            return digits
        
        
        # if the current digit is 9 then set it to 0
        digits[i] = 0
        
    # If all digits were 9, we need to add a new digit at the front
    return [1] + digits