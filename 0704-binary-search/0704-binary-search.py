class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] >= target:
                right = mid
            else :
                left = mid+1

        if nums[left] == target :
            return left
        else : return -1
