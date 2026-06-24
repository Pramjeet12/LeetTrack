class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        original = x
        revx = 0
        while x > 0:
            lastdigit = x%10
            revx = revx*10 + lastdigit
            x = x//10

        return original == revx
