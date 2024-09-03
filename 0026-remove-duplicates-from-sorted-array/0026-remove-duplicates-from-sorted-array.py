class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        revisor = 0
        
        for pointer in range(1, len(nums)):
            if nums[revisor] < nums[pointer]:
                revisor += 1
                nums[revisor] = nums[pointer]
        return revisor+1