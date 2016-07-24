"""
class file for containing various string functions
"""


class StringFunctions:

    def __init__(self, str):
        self.str = str

    def hasUniqueChars(self):
        if len(self.str) > 128:
            return False

        total = [False] * 128

        for i in self.str:
            if total[ord(i)] is False:
                total[ord(i)] = True
            else:
                return False
        return True
