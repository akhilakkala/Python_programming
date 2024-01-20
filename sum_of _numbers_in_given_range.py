#By using loop

# x = int(input("Enter the first number in the range : "))
# y = int(input("Enter the second number in the range : "))

# sum = 0
# while y!=x:
#     sum = sum+y
#     y = y-1
# print(sum+y)

# By using recursion

def recursum(sum,num1,num2):
  if num1 > num2:
    return sum
  return num1 + recursum(sum,num1+1,num2)

m = int(input("Enter the first number in the range : "))
n = int(input("Enter the second number in the range : "))
sum = 0
print(recursum(sum,m,n))