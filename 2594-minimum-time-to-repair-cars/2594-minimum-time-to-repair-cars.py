class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
            
        def cars_can_be_fixed(given_time):
            fixed_cars = 0
            for rank in ranks:
                fixed_cars += int(sqrt(given_time // rank))
            if fixed_cars >= cars:
                return True
            else : return False
            
        left, right = min(ranks)*1, max(ranks)*(cars**2)
        while left < right:
            mid = left + (right-left) // 2
            if cars_can_be_fixed(mid):
                right = mid
            else :
                left = mid + 1
            print(left, right)
        return left