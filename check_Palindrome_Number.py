
num = input("Enter any number : ")

# BY STRING SLICING METHOD
rev_num = num[::-1]
if(num==rev_num):
    print(f"The number {num} is a palindrome")
else:
    print(f"{num} Not a palindrome number")
    
# BY USING WHILE LOOP
# num = int(input("Enter any number : "))
# rev_num = 0
# while(num>0):
#     rev_num = (num%10)+rev_num*10
#     num = int(num/10)
    
# print(rev_num)