class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        alt_count, o_count, e_count = 1, 0, 0
        expect_odd = (nums[0]%2 == 0)

        for idx, num in enumerate(nums): 
            # check for alt count
            if (expect_odd and num % 2 == 1) or (not expect_odd and num % 2 == 0):
                alt_count += 1
                expect_odd = not expect_odd

            if num % 2 == 0:
                e_count += 1
            elif num % 2 == 1:
                o_count += 1
        
        return max(alt_count, o_count, e_count)