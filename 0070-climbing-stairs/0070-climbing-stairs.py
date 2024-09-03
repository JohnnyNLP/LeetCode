class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        def combination(n, r):
            top = 1
            bottom = 1
            for i in range(r):
                top *= (n-i)
                bottom *= (r-i)
            return top / bottom
        
        max_two = n//2
        comb = 0
        
        for num_two in range(max_two+1):
            num_one = n - 2*num_two
            comb += combination(num_two+num_one, min(num_two, num_one))
            
        return comb