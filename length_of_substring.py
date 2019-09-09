import os


def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        v = "0"
        li = []
        for i in range(len(s)):
            if s[i] == v[-1]:
                length = len(v) - 1
                li.append(length)
                v = ""
                v += s[i]
            else:
                v += s[i]
        length = len(v) - 1
        li.append(length)
        li.sort()
        return li[-1]
        
 lengthOfLongestSubstring("STRING")
