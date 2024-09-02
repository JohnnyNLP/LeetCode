class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def bloom_simulator(mid):
            # after waiting 'mid' days, we should be able to make 'm' bouquets
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom > mid :
                    flowers = 0
                else : 
                    bouquets += (flowers+1) // k
                    flowers = (flowers+1) % k 
            return bouquets >= m
            
        # check for impossible case... we don't have enough flowers
        if len(bloomDay) < m*k:
            return -1

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = left + (right-left) // 2
            if bloom_simulator(mid):
                right = mid
            else :
                left = mid + 1

        return left