class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        char_set = set()
        for char in s:
            if char not in char_set:
                char_set.add(char)
            else :
                return char