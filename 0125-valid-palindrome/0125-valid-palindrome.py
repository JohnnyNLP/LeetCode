import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        text_only = re.sub("[^0-9a-zA-Z]", "", s).lower()

        if text_only == text_only[::-1] :
            return True
        else : return False