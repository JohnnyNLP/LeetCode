class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        combined_string = ""

        # Sort by length
        longest_word_length = max(set([len(word) for word in words]))
        sorted_list = []

        while longest_word_length > 0 :
            for word in words:
                if len(word) == longest_word_length and word not in sorted_list:
                    sorted_list.append(word)
            longest_word_length -= 1

        # Add longest sequence first
        for word in sorted_list:
            if word+'#' not in combined_string : 
                combined_string += word+'#'
                longest_word_length -= 1

        return len(combined_string)