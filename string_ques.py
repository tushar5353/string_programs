"""
class file for containing various string functions
"""

import string


class StringFunctions:

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def hasUniqueChars(self):
        """
        function to determine if the string is having all the characters as 
        unique or not.
        """
        if len(self.str1) > 128:
            return False

        total = [False] * 128

        for i in self.str1:
            if total[ord(i)] is False:
                total[ord(i)] = True
            else:
                return False
        return True


    def stringPermutation(self):
        """
        function to determine if two string are in permutation or not.
        """
        if len(self.str1) != len(self.str2):
            return False
        else:
            return "".join(sorted(self.str1)) == "".join(sorted(self.str2))


    def urlifyString(self):
        """
        function to replace space with %20.
        """
        res = ""
        start = False

        for i in reversed(self.str1):
            if i != ' ':
                start = True

            if (i == ' '  and start is True):
                res += '02%'
            else:
                res += i
        return res[::-1]


    def isPermutationPalindrome(self):
        d = dict.fromkeys(string.ascii_lowercase, False)
        count = 0
        for i in self.str1:
            if(ord(i)>97 and ord(i)<123):
                d[i] = not d[i]

        for key in d:
            if d[key] == True:
                count += 1
                if count > 1:
                    return False
        return True
