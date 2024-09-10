class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        def count_less_equal(mid):
            sums = [0]
            for row in mat:
                new_sums = []
                for current_sum in sums:
                    for value in row:
                        new_sum = current_sum + value
                        if new_sum <= mid:
                            new_sums.append(new_sum)
                # Keep only the smallest k sums to avoid unnecessary computations
                new_sums.sort()
                sums = new_sums[:k]
                if len(sums) >= k and sums[k-1] > mid:
                    break
            return len(sums) >= k
            
        max_sum = sum(max(row) for row in mat)
        min_sum = sum(min(row) for row in mat)
        
        left, right = min_sum, max_sum

        while left < right:
            mid = left + (right-left) // 2
            if count_less_equal(mid):
                right = mid
            else :
                left = mid+1
        
        return left
