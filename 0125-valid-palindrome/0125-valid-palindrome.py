import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        text_only = re.sub("[^0-9a-zA-Z]", "", s).lower()
        mid_point = len(text_only)//2

        left_half = text_only[:mid_point]
        right_half = ''.join(reversed(text_only))[:mid_point]

        if left_half == right_half :
            return True
        else : return False