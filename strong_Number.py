
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_strong_number(num):
    original_num = num
    total = 0

    while num > 0:
        digit = num % 10
        total += factorial(digit)
        num //= 10

    return original_num == total

num = int(input("Enter any positive Number: "))

if is_strong_number(num):
    print(f"The {num} is a strong number")
else:
    print(f"The number {num} is not a strong number")

# num = int(input("Enter any positive Number : "))
# x = num
# total = 0
# while(num>0):
#     n = num%10
#     val = 1
#     while n >1:
#         val *= n
#         n = n-1
#     total +=val
#     num //=10   
# if(x==total):
#     print(f"The {x} is a strong number")
# else:
#     print(f"The number {x} is not a strong number") 
    
