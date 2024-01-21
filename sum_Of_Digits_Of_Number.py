num = int(input("Enter any number : "))
x = num
sum = 0

# BY RECURRSION
def sum_Of_Digits(num , sum):
    if(num==0):
        return sum
    sum += int(num%10)
    return sum_Of_Digits(int(num/10),sum)

print(f"The sum of digits in the number {x} is" , sum_Of_Digits(num,sum))

# BY BRUTE FORCE APPROACH
# while(num!=0):
#     sum = sum + int(num%10)
#     num = num/10

# print(f"The sum of digits in the number {x} is {(sum)}")