class Solution:
    def minSteps(self, n: int) -> int:
         res = 0
         i = 2
         while n > 0 and i <= n:
             while n % i == 0:
                 res += i
                 n //= i
             i += 1
        
         return res