"""
Given an input string, write a function that returns the Run Length Encoded string for the input string.

For example, if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6”.

"""

string = "wwwwaaadexxxxxx"
encoded_string = ""
counter = 1
word_count = 1
for i in string:
    if counter == len(string):
        encoded_string += str(word_count) + i
        print(encoded_string)
        break
    if i != string[counter]:
        encoded_string += str(word_count) + i
        word_count = 1
    else:
        word_count = word_count + 1
    counter = counter + 1

