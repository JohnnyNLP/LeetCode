class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 2 : return 2

        alt_count, o_count, e_count = 1, 0, 0
        # initial case setup
        expect_odd = (nums[0]%2 == 0)
        if expect_odd : e_count += 1
        else : o_count += 1

        for idx, num in enumerate(nums): 
            # check for even-odd alt
            if expect_odd and num % 2 == 1:
                alt_count += 1
                expect_odd = False
            # check for odd-even alt
            elif not expect_odd and num % 2 == 0:
                alt_count += 1
                expect_odd = True
            
            if idx > 0 and num % 2 == 0:
                e_count += 1
            elif idx > 0 and num % 2 == 1:
                o_count += 1
        
        return max(alt_count, o_count, e_count)

                