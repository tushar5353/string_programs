

def get_count(str):
    count = 0
    for i in str:
        count += 1
    return count

def reverse(str, count):
    x=""
    for i in range(1,count+1):
        x=x + str[-i]
    return x

str = "abc"
count = get_count(str)
x = reverse(str,count)
print(x)
