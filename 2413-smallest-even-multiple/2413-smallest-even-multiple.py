class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(2,n+1):
            if 2%i==0 and n%i==0:
                return int(n)
        return 2*n