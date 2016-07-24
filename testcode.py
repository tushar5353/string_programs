import string_ques

str1 = "as df    "
str2 = "asodf"

str_func_obj = string_ques.StringFunctions(str1, str2)

print("Test for unique Characters in a string:")
print(str_func_obj.hasUniqueChars())

print("Test for permutation in two strings:")
print(str_func_obj.stringPermutation())

print("urilifying a string:")
print(str_func_obj.urlifyString())
