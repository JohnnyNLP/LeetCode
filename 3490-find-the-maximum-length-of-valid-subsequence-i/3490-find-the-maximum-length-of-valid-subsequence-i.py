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
            # check for alt count
            if (expect_odd and num % 2 == 1) or (not expect_odd and num % 2 == 0):
                alt_count += 1
                expect_odd = not expect_odd

            if idx > 0 and num % 2 == 0:
                e_count += 1
            elif idx > 0 and num % 2 == 1:
                o_count += 1
        
        print(alt_count, o_count, e_count)
        return max(alt_count, o_count, e_count)

                