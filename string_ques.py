"""
class file for containing various string functions
"""


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

