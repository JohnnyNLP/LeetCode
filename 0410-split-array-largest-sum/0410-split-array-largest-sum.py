class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def split_simulator(mid, nums, k):
            total = 0
            sub_array_num = 1
            
            for num in nums:
                # add num while you can
                if total+num <= mid :
                    total += num
                # if the element is bigger than the mid? : increase mid
                elif num > mid :
                    return False
                # jump to the next subarray and add again
                else :
                    total = num
                    sub_array_num += 1
                
            
            # if number of subarrays are reached: try less threshold
            if sub_array_num <= k :
                return True
            # else: try bigger threshold
            else : return False

        left, right = min(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            print(left, mid, right)
            if split_simulator(mid, nums, k):
                right = mid
            else :
                left = mid+1
        return left
        