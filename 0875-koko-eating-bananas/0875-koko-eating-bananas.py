class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def get_hour_per_pile(pile, mid):
            quotient = pile//mid
            remainder = pile % mid
            # if there's more banana in the file
            if remainder != 0: return quotient + 1
            else : return quotient
        
        def eat_all_bananas(piles, mid):
            total_time = 0
            for pile in piles :
                total_time += get_hour_per_pile(pile, mid)
            return total_time

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right-left)//2
            total_time = eat_all_bananas(piles, mid)

            if total_time <= h:
                right = mid
            else :
                left = mid + 1

        return left