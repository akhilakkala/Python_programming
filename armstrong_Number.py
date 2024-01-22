n = int(input("Enter a number : "))
num = n
l = len(str(n))
sum = 0
while(num>0):
    dig = int(num%10)
    num = num/10
    sum = pow(dig,l) + sum
if(sum==n):
    print(f"The number {n} is palindrome")
else:
    print(f"{n} is not a palindrome")