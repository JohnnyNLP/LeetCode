class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits[-1] = digits[-1] + 1

        # If there's any 10 in the list iterate
        while any([1 for digit in digits if digit == 10]) :
            target_idx = digits.index(10)
            digits[target_idx] = 0

            if target_idx-1 >= 0 :
                digits[target_idx-1] = digits[target_idx-1] + 1
            else :
                digits.insert(0, 1)

        return digits
            
   