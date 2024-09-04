class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        def day_simulator(pointer, capacity, days) :
            # simulate each day
            day = 1
            total = 0
            for weight in weights :
                # Load if you can
                if total+weight <= capacity :
                    total += weight
                # Skip the day if you can't
                else :
                    day += 1
                    total = weight

            # Enough day to deliever all weights -> try less capacity
            if day <= days:
                return True
            # Not enough day for all weights -> try more capacity
            else :
                return False

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            print(left, mid, right)
            if day_simulator(0, mid, days):
                right = mid
            else:
                left = mid + 1
        return left

                            

        