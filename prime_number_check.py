
n = int(input("Enter any number : "))

# BY OPTIMIZATION BY ROOT N
flag = 0
if n<2:
  flag = 1
else:
  for i in range(2,int(pow(n,0.5)+1)):
    if n%i==0:
      flag = 1
      break

if flag == 1:
    print(f"The number {n} is not a prime number")
else:
    print(f"The number {n} is a prime number")

# BY BASIC ITERATION

# bool = 0
# if n==2:
#     bool =1
# for i in range(2,n):
#     if n%i==0:
#         break
#     else:
#         bool = 1
        
# if (bool==0):
#     print(f"The number {n} is not a prime number")
# else:
#     print(f"The number {n} is a prime number")
    