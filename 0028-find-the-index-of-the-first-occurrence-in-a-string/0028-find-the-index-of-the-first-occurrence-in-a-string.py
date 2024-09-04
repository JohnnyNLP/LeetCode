class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        
        pointer = 0
        while pointer < len(haystack):
            if haystack[pointer:pointer+len(needle)] == needle:
                print(haystack[pointer:max(pointer+len(needle), len(haystack))])
                return pointer
            else : pointer += 1
        

