x = int(input("Enter the first number in the range : "))
y = int(input("Enter the second number in the range : "))

prime_nums = []

# THE OPTIMIZE CODE
for num in range(x, y + 1):
    flag = 0
    
    if num < 2:
        flag = 1
        
    if num % 2 == 0:
        continue
        
    if num % 3 == 0:
        continue
        
    iter = 2
    while iter < int(pow(num, 0.5)):
        if num % iter == 0:
            flag = 1
            break
        iter += 1
        
    if flag == 0:
        prime_nums.append(num)

print(prime_nums)

# BRUTE FORCE APPROACH
# for i in range(x,y+1):
#     bool = 0
    
#     if i<2:
#         continue
#     if i==2:
#         prime_nums.append(2)
#         continue
#     for m in range(2,i):
#         if i%m==0:
#             bool=1
#             break
        
#     if bool ==0:
#         prime_nums.append(i)
# print(prime_nums)
        
