# By using While loop

# x = int(input("Enter a number: "))
# sum = 0
# while x > 0:
#     sum += x
#     x = x-1

# print(sum)

# By Recurrsion

def getSum(num):
    if num==1:
        return 1
    return num + getSum(num-1)

n = int(input("Enter any number : "))
print(getSum(n))