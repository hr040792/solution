class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: #0 and 1 square root is same in this code
            return x

        left, right = 1,x//2 #sqrt never more then x/2 

        while left <= right:
            mid = (left + right)//2
            square = mid * mid 
            
            if square == x: #perfect square
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid -1

        #right is floor(sqrt(x)) when loop end
        return right
        