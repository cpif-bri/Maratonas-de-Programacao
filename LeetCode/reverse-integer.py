class Solution:
    def reverse(x: int) -> int:
        if(x < 0):
            newInt = int((str(x)[1:])[::-1]) * -1
            if(newInt < -2147483647):
                return 0
            return newInt
        else:
            newInt = int(str(x)[::-1])
            if(newInt > 2147483647):
                return 0
            return newInt
        
while(True):
    x = int(input())
    print(Solution.reverse(x))