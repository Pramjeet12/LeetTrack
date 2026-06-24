class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
           sign = -1
        else:
            sign = 1
        x = abs(x)

        revx = 0
        while x > 0:
              lastdigit = x%10
              revx = revx*10 + lastdigit
              x = x//10
        revx = sign * revx

        if revx < -2**31 or revx > 2**31 - 1:
           return 0

        return revx
     